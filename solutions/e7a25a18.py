def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def crop(g, cells):
    a, b, c, d = bbox(cells)
    return [list(row[c : d + 1]) for row in g[a : b + 1]]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    frame = crop(g, points(g, 2))
    inside = [row[1:-1] for row in frame[1:-1]]
    template = crop(
        inside, [(r, c) for r, row in enumerate(inside) for c, v in enumerate(row) if v != 0]
    )
    h, w = (len(inside), len(inside[0]))
    a, b = (len(template), len(template[0]))
    if h % a or w % b:
        raise ValueError("Noninteger block scale")
    filled = [[v for v in row for _ in range(w // b)] for row in template for _ in range(h // a)]
    return [[2] * (w + 2)] + [[2] + row + [2] for row in filled] + [[2] * (w + 2)]
