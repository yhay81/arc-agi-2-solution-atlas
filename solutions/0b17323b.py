def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    out = copy(g)
    ps = sorted(((r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v))
    dr = ps[1][0] - ps[0][0]
    dc = ps[1][1] - ps[0][1]
    r, c = ps[-1]
    while 0 <= r + dr < len(g) and 0 <= c + dc < len(g[0]):
        r += dr
        c += dc
        out[r][c] = 2
    return out
