def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    out = copy(g)
    ps = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 2]
    a, b = ps[0]
    z, d = ps[-1]
    dr = (z > a) - (z < a)
    dc = (d > b) - (d < b)
    r, c = (a, b)
    for _ in range(max(abs(z - a), abs(d - b)) + 1):
        out[r][c] = 3 if g[r][c] == 1 else 2
        r += dr
        c += dc
    return out
