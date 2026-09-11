from collections import Counter


def bbox(ps):
    return (
        min((r for r, c in ps)),
        min((c for r, c in ps)),
        max((r for r, c in ps)),
        max((c for r, c in ps)),
    )


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    shapes = []
    for color in {v for row in g for v in row if v != bg(g)}:
        top, left, bottom, right = bbox(
            [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]
        )
        shapes.append((bottom - top + 1, right - left + 1, color))
    h = max(x[0] for x in shapes)
    w = max(x[1] for x in shapes)
    out = [[8] * w for _ in range(h)]
    for a, b, col in sorted(shapes, key=lambda x: x[0] * x[1], reverse=True):
        for r in range(a):
            for c in range(b):
                out[r][c] = col
    return out
