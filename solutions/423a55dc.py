def solve(grid):
    g = grid
    end = max((r for r, row in enumerate(g) if any(row)))
    out = [[0] * len(g[0]) for _ in g]
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            if 0 <= c - (end - r) < len(row):
                out[r][c - (end - r)] = v
    return out
