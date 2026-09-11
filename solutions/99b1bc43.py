def _xor_separated_panels(grid):
    height, width = len(grid), len(grid[0])
    separator = height // 2
    if height % 2 == 0 or grid[separator][0] == 0 or len(set(grid[separator])) != 1:
        return [row[:] for row in grid]
    top, bottom = grid[:separator], grid[separator + 1 :]
    if len(top) != len(bottom):
        return [row[:] for row in grid]
    return [
        [3 if (a != 0) != (b != 0) else 0 for a, b in zip(ra, rb)] for ra, rb in zip(top, bottom)
    ]


def solve(grid):
    return _xor_separated_panels(grid)
