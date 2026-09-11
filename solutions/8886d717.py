def solve(grid):
    a = grid
    a = [row[:] for row in a]
    if all(v == 9 for v in a[0]) or all(v == 9 for v in a[-1]):
        return [list(row) for row in zip(*solve([list(row) for row in zip(*a)]))]
    if all(row[0] == 9 for row in a):
        return [row[::-1] for row in solve([row[::-1] for row in a])]
    out = [row[:] for row in a]
    for r, row in enumerate(a):
        for c, v in enumerate(row):
            if v != 8:
                continue
            near = any(
                0 <= r + dy < len(a) and 0 <= c + dx < len(a[0]) and a[r + dy][c + dx] == 2
                for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]
            )
            if near:
                out[r][c] = 2
            elif c + 1 < len(a[0]) - 1:
                out[r][c + 1] = 8
    return out
