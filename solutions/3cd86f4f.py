def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    out = [[0] * (w + h - 1) for _ in range(h)]
    for r in range(h):
        out[r][h - 1 - r : h - 1 - r + w] = a[r][:]
    return out
