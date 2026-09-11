def solve(grid):
    return [row + row[::-1] for row in grid]
