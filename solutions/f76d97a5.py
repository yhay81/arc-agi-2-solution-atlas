def _marker_mask_other_color(grid):
    colors = {value for row in grid for value in row if value not in (0, 5)}
    if len(colors) != 1:
        return [row[:] for row in grid]
    color = next(iter(colors))
    return [[color if value == 5 else 0 for value in row] for row in grid]


def solve(grid):
    return _marker_mask_other_color(grid)
