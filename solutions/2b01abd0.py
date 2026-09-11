def solve(grid):
    output = [row[:] for row in grid]
    full_rows = [r for r, row in enumerate(grid) if all(value == 1 for value in row)]
    full_columns = [c for c in range(len(grid[0])) if all(row[c] == 1 for row in grid)]
    colors = sorted({value for row in grid for value in row if value not in (0, 1)})
    swap = {colors[0]: colors[1], colors[1]: colors[0]}
    if full_rows:
        axis = full_rows[0]
        source = [
            (r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value in swap
        ]
        for r, c in source:
            output[r][c] = swap[grid[r][c]]
            output[2 * axis - r][c] = grid[r][c]
    else:
        axis = full_columns[0]
        source = [
            (r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value in swap
        ]
        for r, c in source:
            output[r][c] = swap[grid[r][c]]
            output[r][2 * axis - c] = grid[r][c]
    return output
