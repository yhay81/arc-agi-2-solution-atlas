def solve(grid):
    width = len(grid[0])
    return [row[: width // 3] for row in grid] if width % 3 == 0 else [row[:] for row in grid]
