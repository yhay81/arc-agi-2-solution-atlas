def _extend_vertical_period(grid):
    height, width = len(grid), len(grid[0])
    period = height
    for candidate in range(1, height + 1):
        if all(grid[row] == grid[row % candidate] for row in range(height)):
            period = candidate
            break
    return [grid[row % period][:] for row in range(height + width)]


def solve(grid):
    return [[2 if value == 1 else 0 for value in row] for row in _extend_vertical_period(grid)]
