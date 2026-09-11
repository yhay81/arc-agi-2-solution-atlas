def solve(grid):
    g = grid
    o = [[5] * len(g[0]) for _ in g]
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            if v and c:
                o[r][c - 1] = v
    return o
