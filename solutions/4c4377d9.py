def solve(grid):
    return grid[::-1] + [row[:] for row in grid]
