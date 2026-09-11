def _fill_active_columns_tile2(grid):
    filled = [row[:] for row in grid]
    for col in range(len(grid[0])):
        if any(row[col] for row in grid):
            for row in filled:
                if row[col] == 0:
                    row[col] = 8
    return [row + row for row in filled] + [row + row for row in filled]


def solve(grid):
    return _fill_active_columns_tile2(grid)
