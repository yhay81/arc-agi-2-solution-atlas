def solve(grid):
    out = [row[:] for row in grid]
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == 5:
                if grid[r][0] in (0, 5):
                    raise ValueError("Gray cell has no row color instruction")
                out[r][c] = grid[r][0]
    return out
