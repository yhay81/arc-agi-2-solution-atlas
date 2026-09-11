def solve(grid):
    if not grid or not grid[0]:
        return [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    rows = [row for row in range(height) if len(set(grid[row])) == 1 and grid[row][0] != 0]
    cols = [
        col
        for col in range(width)
        if len({grid[r][col] for r in range(height)}) == 1 and grid[0][col] != 0
    ]
    if not rows or not cols:
        return [row[:] for row in grid]
    row_edges, col_edges = ([-1, *rows, height], [-1, *cols, width])
    row_intervals = [
        (row_edges[i] + 1, row_edges[i + 1])
        for i in range(len(row_edges) - 1)
        if row_edges[i + 1] > row_edges[i] + 1
    ]
    col_intervals = [
        (col_edges[i] + 1, col_edges[i + 1])
        for i in range(len(col_edges) - 1)
        if col_edges[i + 1] > col_edges[i] + 1
    ]
    if not row_intervals or not col_intervals:
        return [row[:] for row in grid]
    cell_shapes = {
        (bottom - top, right - left)
        for top, bottom in row_intervals
        for left, right in col_intervals
    }
    if len(cell_shapes) != 1:
        return [row[:] for row in grid]
    cells = [
        [row[left:right] for row in grid[top:bottom]]
        for top, bottom in row_intervals
        for left, right in col_intervals
    ]
    color_counts = [len({value for row in cell for value in row}) for cell in cells]
    minimum = min(color_counts)
    if color_counts.count(minimum) != 1:
        return [row[:] for row in grid]
    key = cells[color_counts.index(minimum)]
    if (len(key), len(key[0])) != (len(row_intervals), len(col_intervals)):
        return [row[:] for row in grid]
    output = [[0] * width for _ in range(height)]
    for row in rows:
        output[row] = grid[row][:]
    for col in cols:
        for row in range(height):
            output[row][col] = grid[row][col]
    for row_index, (top, bottom) in enumerate(row_intervals):
        for col_index, (left, right) in enumerate(col_intervals):
            for r in range(top, bottom):
                output[r][left:right] = [key[row_index][col_index]] * (right - left)
    return output
