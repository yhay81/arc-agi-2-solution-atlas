def solve(grid):
    output = [[0] * len(grid[0])] + [row[:] for row in grid[:-1]]
    return [[2 if value == 8 else 0 for value in row] for row in output]
