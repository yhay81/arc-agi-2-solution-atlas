def solve(grid):
    return [[5 if cell == 7 else cell for cell in row] for row in grid]
