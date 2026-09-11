def _extract_full_line_color(grid):
    for col in range(len(grid[0])):
        if grid[0][col] and all(row[col] == grid[0][col] for row in grid):
            return [[grid[0][col]]]
    for row in grid:
        if row[0] and all(value == row[0] for value in row):
            return [[row[0]]]
    return [row[:] for row in grid]


def solve(grid):
    return _extract_full_line_color(grid)
