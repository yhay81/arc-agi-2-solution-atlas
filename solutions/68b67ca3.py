def _remove_uniform_lines(grid):
    rows = [row for row in grid if len(set(row)) != 1]
    cols = [c for c in range(len(grid[0])) if len({row[c] for row in grid}) != 1]
    return [[row[c] for c in cols] for row in rows] if rows and cols else [row[:] for row in grid]


def solve(grid):
    return _remove_uniform_lines(grid)
