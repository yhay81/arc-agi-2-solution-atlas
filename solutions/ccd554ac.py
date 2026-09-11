def solve(grid):
    height, width = len(grid), len(grid[0])
    return [
        [grid[r % height][c % width] for c in range(width * width)] for r in range(height * height)
    ]
