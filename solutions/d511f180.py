def solve(grid):
    return [[8 if cell == 5 else 5 if cell == 8 else cell for cell in row] for row in grid]
