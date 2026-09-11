def solve(grid):
    g = grid
    n = len(g)
    out = [[0] * (2 * n) for _ in range(2 * n)]
    palette = [g[0][0], g[n // 2][n // 2], g[0][1]]
    for r in range(2 * n):
        for c in range(2 * n):
            out[r][c] = g[r][c] if r < n and c < n else palette[(max(r, c) - n + (r == c)) % 3]
    return out
