def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def empty(g, color=0):
    return [[color] * len(g[0]) for _ in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def solve(grid):
    g = grid
    ps = points(g, 7)
    a, b, c, d = bbox(ps)
    out = empty(g)
    step = d - c + 2
    height = b - a + 2
    for n, left in enumerate(range(c, len(g[0]), step)):
        color = 6 if n % 3 == 2 else 7
        for top in range(a, len(g), height) if color == 6 else [a]:
            for r, col in ps:
                put(out, top + r - a, left + col - c, color)
    return out
