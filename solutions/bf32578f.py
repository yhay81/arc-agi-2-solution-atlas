def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    ps = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v]
    axis = 2 * max((c for r, c in ps)) + 1
    out = [[0] * len(g[0]) for _ in g]
    color = g[ps[0][0]][ps[0][1]]
    for r in sorted({r for r, c in ps}):
        edge = max((c for rr, c in ps if rr == r))
        for c in range(edge + 1, axis - edge):
            put(out, r, c, color)
    return out
