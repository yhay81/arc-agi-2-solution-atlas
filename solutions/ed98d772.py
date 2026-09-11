def _rot(a):
    return [list(x) for x in zip(*a)][::-1]


def solve(grid):
    if len(grid) != len(grid[0]):
        return [row[:] for row in grid]
    r1 = _rot(grid)
    r2 = _rot(r1)
    r3 = _rot(r2)
    return [a + b for a, b in zip(grid, r1)] + [a + b for a, b in zip(r2, r3)]
