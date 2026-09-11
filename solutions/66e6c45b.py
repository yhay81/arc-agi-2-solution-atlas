from collections import Counter


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


def bg(g):
    return Counter(v for r in g for v in r).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    b = bg(g)
    p = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != b}
    a, bb, c, d = box(p)
    o = cp(g)
    paint(o, p, b)
    for r, z in p:
        o[0 if r < (a + bb) / 2 else len(g) - 1][0 if z < (c + d) / 2 else len(g[0]) - 1] = g[r][z]
    return o
