def solve(grid):
    return [[0] * len(grid[0])] + [row[:] for row in grid[:-1]]
