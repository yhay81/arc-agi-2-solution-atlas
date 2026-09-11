def solve(grid):
    return [[2 if cell == 6 else cell for cell in row] for row in grid]
