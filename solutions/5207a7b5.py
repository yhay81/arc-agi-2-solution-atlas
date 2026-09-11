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


def paint(g, p, color):
    for r, c in p:
        if 0 <= r < len(g) and 0 <= c < len(g[0]):
            g[r][c] = color
    return g


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    p = pts(g, 5)
    a, b, c, d = box(p)
    n = b - a + 1
    o = cp(g)
    for z in range(len(g[0])):
        if z == c:
            continue
        height = n - 2 * (z - c)
        paint(o, {(r, z) for r in range(a, min(a + height, len(g)))}, 8 if z < c else 6)
    return o
