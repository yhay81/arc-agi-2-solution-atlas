def _nonzero_row(grid):
    values = [v for row in grid for v in row if v]
    return [values] if values else [row[:] for row in grid]


def solve(grid):
    return _nonzero_row(grid)
