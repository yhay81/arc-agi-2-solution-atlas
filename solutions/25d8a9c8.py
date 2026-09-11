def solve(grid):
    return [[5 if len(set(row)) == 1 else 0] * len(grid[0]) for row in grid]
