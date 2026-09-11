def _mirror_threefold(grid):
    horizontal = [row[::-1] + row + row[::-1] for row in grid]
    return horizontal[::-1] + horizontal + horizontal[::-1]


def solve(grid):
    return _mirror_threefold(grid)
