def solve(grid):
    g = grid
    k = max((c for r, row in enumerate(g) for c, v in enumerate(row) if v != 0)) + 1
    w = len(g[0])
    return [row[:k] + [row[k - 1]] * (w - 2 * k) + row[:k] for row in g]
