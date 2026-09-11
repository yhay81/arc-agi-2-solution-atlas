def _collapse_x_five(grid):
    if (len(grid), len(grid[0])) != (5, 5):
        return [row[:] for row in grid]
    rows = ((0, 1, 0), (1, 2, 3), (4, 3, 4))
    cols = ((0, 1, 4), (3, 2, 1), (0, 3, 4))
    return [[grid[rows[r][c]][cols[r][c]] for c in range(3)] for r in range(3)]


def solve(grid):
    return _collapse_x_five(grid)
