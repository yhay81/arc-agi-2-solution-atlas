def solve(grid):
    g = grid
    n = len(g[0])
    mid = n // 2
    out = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if abs(c - mid) == r:
                out[r][c] = 2
            elif r > abs(c - mid) and (r - c + mid) % 4 == 0:
                out[r][c] = 1
    return out
