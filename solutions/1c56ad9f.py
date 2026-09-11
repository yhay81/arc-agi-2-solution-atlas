def solve(grid):
    g = grid
    out = [[0] * len(g[0]) for _ in g]
    end = max((r for r, row in enumerate(g) if any(row)))
    for r, row in enumerate(g):
        d = [0, -1, 0, 1][(end - r) % 4]
        for c, v in enumerate(row):
            if 0 <= c + d < len(row):
                out[r][c + d] = v
    return out
