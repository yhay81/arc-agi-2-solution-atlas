def _scale_by_color_count(grid):
    colors = {v for row in grid for v in row if v}
    if not len(colors):
        return [row[:] for row in grid]
    factor = len(colors)
    return [[v for v in row for _ in range(factor)] for row in grid for _ in range(factor)]


def solve(grid):
    return _scale_by_color_count(grid)
