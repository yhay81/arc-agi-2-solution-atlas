def solve(grid):
    a = grid
    out = [row[:] for row in a]
    for r in range(len(a) - 1):
        for c in range(len(a[0]) - 1):
            out[r][c] = a[r][-1] if a[r][-1] == a[-1][c] else 0
    return out
