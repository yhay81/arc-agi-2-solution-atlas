def solve(grid):
    return [row[:] for row in grid] + [row[:] for row in grid[::-1]]
