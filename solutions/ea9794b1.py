def solve(grid):
    g = grid
    h, w = (len(g) // 2, len(g[0]) // 2)
    out = [[0] * w for _ in range(h)]
    for dr, dc in ((0, 0), (1, 1), (1, 0), (0, 1)):
        for r in range(h):
            for c in range(w):
                if g[r + dr * h][c + dc * w]:
                    out[r][c] = g[r + dr * h][c + dc * w]
    return out
