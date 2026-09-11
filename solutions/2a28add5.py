def solve(grid):
    a = grid
    out = [[7] * len(a[0]) for _ in a]
    for r, row in enumerate(a):
        mark = [i for i, value in enumerate(row) if value == 6]
        if not len(mark):
            continue
        if not (len(mark) == 1):
            raise ValueError("task assumptions are not satisfied")
        c = mark[0]
        left = sum(value != 7 for value in row[:c])
        right = sum(value != 7 for value in row[c + 1 :])
        out[r][c - left : c + right + 1] = [8] * (left + right + 1)
    return out
