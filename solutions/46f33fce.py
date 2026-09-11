def _sample_odd_cells_scale_four(grid):
    if len(grid) < 2 or len(grid[0]) < 2:
        return [row[:] for row in grid]
    sampled = [row[1::2] for row in grid[1::2]]
    return [[value for value in row for _ in range(4)] for row in sampled for _ in range(4)]


def solve(grid):
    return _sample_odd_cells_scale_four(grid)
