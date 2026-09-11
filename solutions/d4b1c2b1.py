def solve(grid):
    factor = len({cell for row in grid for cell in row})
    return [[cell for cell in row for _ in range(factor)] for row in grid for _ in range(factor)]
