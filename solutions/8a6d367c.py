from collections import Counter


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def crop(g, cells):
    a, b, c, d = bbox(cells)
    return [list(row[c : d + 1]) for row in g[a : b + 1]]


def solve(grid):
    g = grid
    background = bg(g)
    colors = set(sum(g, [])) - {background}
    wall = max(
        colors,
        key=lambda v: (lambda box: (box[1] - box[0] + 1) * (box[3] - box[2] + 1))(
            bbox(points(g, v))
        ),
    )
    a, b, c, d = bbox(points(g, wall))
    h, w = (b - a - 1, d - c - 1)
    inside = [row[c + 1 : d] for row in g[a + 1 : b]]
    fillset = set(sum(inside, [])) - {background}
    if len(fillset) != 1:
        raise ValueError("Ambiguous clue color")
    fill = fillset.pop()
    choices = []
    for color in colors - {wall, fill}:
        patch = crop(g, points(g, color))
        ph, pw = (len(patch), len(patch[0]))
        if h % ph or w % pw:
            continue
        scaled = [
            [
                fill if patch[r // (h // ph)][col // (w // pw)] == color else background
                for col in range(w)
            ]
            for r in range(h)
        ]
        if all(
            (
                v == background or scaled[r][col] == fill
                for r, row in enumerate(inside)
                for col, v in enumerate(row)
            )
        ):
            choices.append(scaled)
    if len(choices) != 1:
        raise ValueError("No unique compatible template")
    return [[wall] * (w + 2)] + [[wall] + row + [wall] for row in choices[0]] + [[wall] * (w + 2)]
