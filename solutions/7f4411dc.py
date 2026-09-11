def _keep_solid_rectangle_cells(grid):
    keep = [[False] * len(grid[0]) for _ in grid]
    for row in range(len(grid) - 1):
        for col in range(len(grid[0]) - 1):
            value = grid[row][col]
            if value and all(grid[r][c] == value for r in (row, row + 1) for c in (col, col + 1)):
                for r in (row, row + 1):
                    for c in (col, col + 1):
                        keep[r][c] = True
    return [
        [value if keep[r][c] else 0 for c, value in enumerate(row)] for r, row in enumerate(grid)
    ]


def solve(grid):
    return _keep_solid_rectangle_cells(grid)
