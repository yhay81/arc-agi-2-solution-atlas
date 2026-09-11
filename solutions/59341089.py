def solve(grid):
    return [row[::-1] + row + row[::-1] + row for row in grid]
