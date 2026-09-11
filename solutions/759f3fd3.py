def solve(grid):
    a = grid
    r = next(i for i, row in enumerate(a) if all(v == 3 for v in row))
    c = next(j for j in range(len(a[0])) if all(row[j] == 3 for row in a))
    out = [row[:] for row in a]
    for y, row in enumerate(a):
        for x, value in enumerate(row):
            if value != 0:
                continue
            if max(abs(y - r), abs(x - c)) % 2 == 0:
                out[y][x] = 4
    return out
