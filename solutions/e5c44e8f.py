def solve(grid):
    a = grid
    r, c = next((r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == 3)
    out = [row[:] for row in a]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(4 * max(len(a), len(a[0]))):
        dy, dx = dirs[i % 4]
        length = 2 * (i // 2 + 1)
        for _ in range(length):
            r, c = (r + dy, c + dx)
            if 0 <= r < len(a) and 0 <= c < len(a[0]):
                if a[r][c] == 2:
                    return out
                out[r][c] = 3
    return out
