def solve(grid):
    height, width = len(grid), len(grid[0])
    uniform_rows = [grid[row][0] for row in range(height) if len(set(grid[row])) == 1]
    uniform_cols = [
        grid[0][col] for col in range(width) if len({grid[row][col] for row in range(height)}) == 1
    ]
    line_values = set(uniform_rows) & set(uniform_cols)
    nonzero = line_values - {0}
    if len(nonzero) == 1:
        separator = next(iter(nonzero))
    elif len(line_values) == 1:
        separator = next(iter(line_values))
    else:
        return [row[:] for row in grid]
    counts = {}
    for row in grid:
        for value in row:
            if value != separator:
                counts[value] = counts.get(value, 0) + 1
    if not counts:
        return [row[:] for row in grid]
    background = max(counts, key=counts.get)
    row_separators = [
        row for row in range(height) if grid[row][0] == separator and len(set(grid[row])) == 1
    ]
    col_separators = [
        col
        for col in range(width)
        if grid[0][col] == separator and len({grid[row][col] for row in range(height)}) == 1
    ]
    if len(row_separators) < 2 or len(col_separators) < 2:
        return [row[:] for row in grid]
    if {grid[row][0] for row in row_separators} | {grid[0][col] for col in col_separators} != {
        separator
    }:
        return [row[:] for row in grid]
    row_edges, col_edges = [-1, *row_separators, height], [-1, *col_separators, width]
    row_cells = [
        (top + 1, bottom) for top, bottom in zip(row_edges, row_edges[1:]) if bottom > top + 1
    ]
    col_cells = [
        (left + 1, right) for left, right in zip(col_edges, col_edges[1:]) if right > left + 1
    ]
    if len(row_cells) < 3 or len(col_cells) < 3:
        return [row[:] for row in grid]
    row_indices = [0, (len(row_cells) - 1) // 2, len(row_cells) - 1]
    col_indices = [0, (len(col_cells) - 1) // 2, len(col_cells) - 1]
    output = [row[:] for row in grid]
    changed = False
    for color, row_index, col_index in zip((1, 2, 3), row_indices, col_indices):
        top, bottom = row_cells[row_index]
        left, right = col_cells[col_index]
        for row in range(top, bottom):
            for col in range(left, right):
                if output[row][col] == background:
                    output[row][col] = color
                    changed = True
    return output if changed else [row[:] for row in grid]
