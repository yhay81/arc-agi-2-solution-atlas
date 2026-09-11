def solve(grid):
    height, width = len(grid), len(grid[0])
    rows = [r for r in range(height) if grid[r][0] == grid[r][-1] == 4]
    cols = [c for c in range(width) if grid[0][c] == grid[-1][c] == 4]
    out = [row[:] for row in grid]

    mapping = {0: 8, 8: 0, 6: 7, 7: 6}
    for r in range(height):
        for c in range(width):
            if r in rows or c in cols:
                out[r][c] = mapping.get(grid[r][c], grid[r][c])
    return out
