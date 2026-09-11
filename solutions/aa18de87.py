def solve(grid):
    a = grid
    out = [row[:] for row in a]
    for r, row in enumerate(a):
        ps = [i for i, value in enumerate(row) if value != 0]
        for x, y in zip(ps, ps[1:]):
            if row[x] == row[y]:
                out[r][x + 1 : y] = [2] * (y - x - 1)
    return out
