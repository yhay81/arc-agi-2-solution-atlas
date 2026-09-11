def _reflect_vertical_period(grid):
    height = len(grid)
    if height < 2:
        return [row[:] for row in grid]
    period = [row[:] for row in grid] + [row[:] for row in grid[-2:0:-1]]
    target_height = 4 * height - 3
    return [period[row % len(period)][:] for row in range(target_height)]


def solve(grid):
    return _reflect_vertical_period(grid)
