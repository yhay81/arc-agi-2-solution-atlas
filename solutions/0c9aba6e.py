def solve(grid):
    a = grid
    half = (len(a) - 1) // 2
    return [
        [8 if a[row][col] == 0 and a[row + half + 1][col] == 0 else 0 for col in range(len(a[0]))]
        for row in range(half)
    ]
