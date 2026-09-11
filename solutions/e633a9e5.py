def solve(grid):
    g = grid
    return [[g[r][c] for c in (0, 0, 1, 2, 2)] for r in (0, 0, 1, 2, 2)]
