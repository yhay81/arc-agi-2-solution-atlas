def solve(grid):
    a = grid
    color = next(c for row in a for c in row if c)
    r, c = next((r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v)
    r *= 4
    c *= 4
    out = [[0] * 9 for _ in range(9)]
    out[r][c] = color
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for k in range(32):
        dy, dx = dirs[k % 4]
        for _ in range(2 * (k // 2 + 1)):
            r += dy
            c += dx
            if 0 <= r < 9 and 0 <= c < 9:
                out[r][c] = color
    return out
