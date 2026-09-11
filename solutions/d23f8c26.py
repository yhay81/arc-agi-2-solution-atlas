def _central_column(grid):
    middle = len(grid[0]) // 2
    return [[value if col == middle else 0 for col, value in enumerate(row)] for row in grid]


def solve(grid):
    return _central_column(grid)
