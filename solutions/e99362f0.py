def solve(grid):
    a = grid
    r = next(i for i, row in enumerate(a) if all(v == 4 for v in row))
    c = next(j for j in range(len(a[0])) if all(row[j] == 4 for row in a))
    parts = [
        [row[:c] for row in a[:r]],
        [row[c + 1 :] for row in a[:r]],
        [row[:c] for row in a[r + 1 :]],
        [row[c + 1 :] for row in a[r + 1 :]],
    ]
    out = [[0] * len(parts[0][0]) for _ in parts[0]]
    for color in (2, 9, 7, 8):
        for part in parts:
            for rr, row in enumerate(part):
                for cc, value in enumerate(row):
                    if value == color:
                        out[rr][cc] = color
    return out
