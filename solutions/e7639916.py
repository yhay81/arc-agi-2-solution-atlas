def paint(g, p, color):
    for r, c in p:
        if 0 <= r < len(g) and 0 <= c < len(g[0]):
            g[r][c] = color
    return g


def pts(g, color):
    return {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color}


def box(p):
    return (
        min((r for r, c in p)),
        max((r for r, c in p)),
        min((c for r, c in p)),
        max((c for r, c in p)),
    )


def cp(g):
    return [list(r) for r in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    p = pts(g, 8)
    a, b, c, d = box(p)
    o = cp(g)
    paint(
        o,
        {(r, z) for r in range(a, b + 1) for z in range(c, d + 1) if r in (a, b) or z in (c, d)},
        1,
    )
    paint(o, p, 8)
    return o
