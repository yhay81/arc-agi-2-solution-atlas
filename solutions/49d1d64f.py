def _edge_expand(grid):
    middle = [[row[0]] + row[:] + [row[-1]] for row in grid]
    return [[0] + grid[0][:] + [0]] + middle + [[0] + grid[-1][:] + [0]]


def solve(grid):
    return _edge_expand(grid)
