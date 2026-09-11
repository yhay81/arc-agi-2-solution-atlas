def solve(grid):
    reflected = [row[::-1] for row in grid]
    rows = grid + reflected + grid
    return [row * 3 for row in rows]
