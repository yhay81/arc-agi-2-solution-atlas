def solve(grid):
    a = grid
    out = [[0] * len(a[0]) for _ in a]
    for c, color in enumerate((1, 2, 3, 4)):
        n = sum(value == color for row in a for value in row)
        if n:
            for row in out[-n:]:
                row[c] = color
    return out
