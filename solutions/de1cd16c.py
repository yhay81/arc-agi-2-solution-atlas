def solve(grid):
    row = 8
    col = 8
    height = 1
    width = 1
    output = [line[col : col + width] for line in grid[row : row + height]]
    color_map = {6: 6, 2: 2, 8: 4, 1: 8}
    return [[color_map.get(value, value) for value in line] for line in output]
