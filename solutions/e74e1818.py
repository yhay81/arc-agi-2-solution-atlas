def solve(grid):
    a = grid
    out = [[0] * len(a[0]) for _ in a]
    for color in {v for row in a for v in row if v}:
        rows = [r for r, row in enumerate(a) for v in row if v == color]
        s = min(rows) + max(rows)
        for r, row in enumerate(a):
            for c, value in enumerate(row):
                if value == color:
                    out[s - r][c] = color
    return out
