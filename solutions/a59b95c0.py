def solve(grid):
    g = grid
    n = len({v for row in g for v in row})
    return [row * n for row in g] * n
