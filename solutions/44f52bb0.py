def solve(grid):
    mirror_rows = grid == grid[::-1]
    mirror_columns = all(row == row[::-1] for row in grid)
    return [[1 if mirror_rows and mirror_columns else 7]]
