def solve(grid):
    a = grid
    a = [row[:] for row in a]
    h, w = len(a), len(a[0])
    r, c = next((r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == 8)
    if r == 0:
        return [list(row) for row in zip(*solve([list(col) for col in zip(*a)]))]
    if r == h - 1:
        return [list(row) for row in zip(*solve([list(col) for col in zip(*a)]))]
    if c == w - 1:
        flipped = solve([row[::-1] for row in a])
        return [row[::-1] for row in flipped]
    if not (c == 0):
        raise ValueError("task assumptions are not satisfied")
    out = [[0] * w for _ in a]
    for y in range(h):
        n = a[y].count(1)
        if y == r:
            out[y][0] = 8
            out[y][1 : n + 1] = [1] * n
            out[y][n + 1 : 2 * n + 1] = [9] * n
        else:
            out[y][:n] = [1] * n
    return out
