def solve(grid):
    row = 0
    col = 6
    height = 3
    width = 3
    return [line[col : col + width] for line in grid[row : row + height]]
