def paint(g, p, color):
    for r, c in p:
        if 0 <= r < len(g) and 0 <= c < len(g[0]):
            g[r][c] = color
    return g


def cp(g):
    return [list(r) for r in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    p = [(r, c, v) for r, row in enumerate(g) for c, v in enumerate(row) if v != 7]
    o = cp(g)
    for r, c, v in p:
        o[r][c] = 7
    for r, c, v in p:
        if r == 0:
            q = {(a, b) for a in (1, 2) for b in ((1, 2) if c == 0 else (w - 3, w - 2))}
        else:
            q = (
                {(h - 4, 2), (h - 3, 2), (h - 2, 3)}
                if c == 0
                else {(h - 4, w - 3), (h - 3, w - 3), (h - 2, w - 4)}
            )
        paint(o, q, v)
    return o
