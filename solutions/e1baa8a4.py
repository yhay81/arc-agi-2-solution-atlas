def solve(grid):
    rows = [0] + [r for r in range(1, len(grid)) if grid[r] != grid[r - 1]]
    cols = [0] + [c for c in range(1, len(grid[0])) if any(row[c] != row[c - 1] for row in grid)]
    return [[grid[r][c] for c in cols] for r in rows]
