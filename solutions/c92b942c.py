def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    out = [[a[r % h][c % w] for c in range(3 * w)] for r in range(3 * h)]
    points = [(r, c) for r, row in enumerate(out) for c, value in enumerate(row) if value]
    for r in {r for r, _ in points}:
        for c in range(3 * w):
            if out[r][c] == 0:
                out[r][c] = 1
    for r, c in points:
        for y, x in [(r - 1, c - 1), (r + 1, c + 1)]:
            if 0 <= y < len(out) and 0 <= x < len(out[0]) and out[y][x] == 0:
                out[y][x] = 3
    return out
