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
    o = cp(g)
    for r in range(0, len(g), 5):
        for c in range(0, len(g[0]), 5):
            v = g[r][c]
            if not v:
                continue
            o[r][c] = 0
            paint(
                o,
                {
                    (r + i, c + j)
                    for i in range(1, 5)
                    for j in range(1, 5)
                    if r + i < len(g) and c + j < len(g[0]) and (g[r + i][c + j] == 0)
                },
                v,
            )
    return o
