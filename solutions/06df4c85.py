def solve(grid):
    height, width = len(grid), len(grid[0])
    separator_rows = [
        row for row in range(height) if len(set(grid[row])) == 1 and grid[row][0] != 0
    ]
    separator_cols = [
        col
        for col in range(width)
        if len({grid[r][col] for r in range(height)}) == 1 and grid[0][col] != 0
    ]
    if not separator_rows or not separator_cols:
        return [row[:] for row in grid]
    row_edges = [-1, *separator_rows, height]
    col_edges = [-1, *separator_cols, width]
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
    output = [row[:] for row in grid]
    cell_colors = {}
    for row_index, (top, bottom) in enumerate(row_intervals):
        for col_index, (left, right) in enumerate(col_intervals):
            cell = [row[left:right] for row in grid[top:bottom]]
            values = {value for row in cell for value in row}
            if len(values) == 1 and next(iter(values)) != 0:
                cell_colors[row_index, col_index] = next(iter(values))
    for (row_index, col_index), color in tuple(cell_colors.items()):
        for other_col in range(len(col_intervals)):
            if cell_colors.get((row_index, other_col)) != color:
                continue
            start, stop = sorted((col_index, other_col))
            for middle in range(start + 1, stop):
                if (row_index, middle) not in cell_colors:
                    top, bottom = row_intervals[row_index]
                    left, right = col_intervals[middle]
                    for row in range(top, bottom):
                        output[row][left:right] = [color] * (right - left)
        for other_row in range(len(row_intervals)):
            if cell_colors.get((other_row, col_index)) != color:
                continue
            start, stop = sorted((row_index, other_row))
            for middle in range(start + 1, stop):
                if (middle, col_index) not in cell_colors:
                    top, bottom = row_intervals[middle]
                    left, right = col_intervals[col_index]
                    for row in range(top, bottom):
                        output[row][left:right] = [color] * (right - left)
    return output
