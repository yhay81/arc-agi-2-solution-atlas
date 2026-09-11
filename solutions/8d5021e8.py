def _sandwich_mirror(grid):
    mirrored = [row[::-1] + row for row in grid]
    return mirrored[::-1] + mirrored + mirrored[::-1]


def solve(grid):
    return _sandwich_mirror(grid)
