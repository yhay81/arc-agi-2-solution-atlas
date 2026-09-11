from collections import Counter


def solve(grid):
    height, width = len(grid), len(grid[0])
    separator_rows = [r for r in range(height) if all(value == 0 for value in grid[r])]
    separator_cols = [c for c in range(width) if all(grid[r][c] == 0 for r in range(height))]
    if len(separator_rows) < 2 or len(separator_cols) < 2:
        return [row[:] for row in grid]
    row_edges, col_edges = [-1, *separator_rows, height], [-1, *separator_cols, width]
    row_segments = [
        (start + 1, stop) for start, stop in zip(row_edges, row_edges[1:]) if stop - start > 1
    ]
    col_segments = [
        (start + 1, stop) for start, stop in zip(col_edges, col_edges[1:]) if stop - start > 1
    ]
    if not row_segments or not col_segments:
        return [row[:] for row in grid]
    counts = Counter(value for row in grid for value in row if value != 0)
    if not counts:
        return [row[:] for row in grid]
    background = counts.most_common(1)[0][0]
    marks = {}
    for cell_row, (top, bottom) in enumerate(row_segments):
        for cell_col, (left, right) in enumerate(col_segments):
            for row in range(top, bottom):
                for col in range(left, right):
                    color = grid[row][col]
                    if color != background:
                        marks.setdefault((color, row - top, col - left), []).append(
                            (cell_row, cell_col)
                        )
    output = [row[:] for row in grid]
    for (color, rel_row, rel_col), locations in marks.items():
        if len(locations) < 2:
            continue
        rows, cols = {}, {}
        for cell_row, cell_col in locations:
            rows.setdefault(cell_row, []).append(cell_col)
            cols.setdefault(cell_col, []).append(cell_row)
        for cell_row, columns in rows.items():
            if len(columns) < 2:
                continue
            for cell_col in range(min(columns), max(columns) + 1):
                if cell_row >= len(row_segments) or cell_col >= len(col_segments):
                    continue
                top, bottom = row_segments[cell_row]
                left, right = col_segments[cell_col]
                if (
                    rel_row < bottom - top
                    and rel_col < right - left
                    and output[top + rel_row][left + rel_col] == background
                ):
                    output[top + rel_row][left + rel_col] = color
        for cell_col, row_values in cols.items():
            if len(row_values) < 2:
                continue
            for cell_row in range(min(row_values), max(row_values) + 1):
                if cell_row >= len(row_segments) or cell_col >= len(col_segments):
                    continue
                top, bottom = row_segments[cell_row]
                left, right = col_segments[cell_col]
                if (
                    rel_row < bottom - top
                    and rel_col < right - left
                    and output[top + rel_row][left + rel_col] == background
                ):
                    output[top + rel_row][left + rel_col] = color
    return output
