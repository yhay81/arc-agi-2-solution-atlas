def _shift_cross_by_marker(array, marker_color=5):
    marker = marker_color
    marker_count = sum(row.count(marker) for row in array)
    if not marker_count:
        return [row[:] for row in array]
    colors = {value for row in array for value in row if value not in (0, marker)}
    if len(colors) != 1:
        return [row[:] for row in array]
    color = next(iter(colors))
    row_counts = [sum(value == color for value in row) for row in array]
    col_counts = [sum(row[c] == color for row in array) for c in range(len(array[0]))]
    if not max(row_counts, default=0) or not max(col_counts, default=0):
        return [row[:] for row in array]
    row, col = row_counts.index(max(row_counts)), col_counts.index(max(col_counts))
    moved_row, moved_col = (row + marker_count, col - marker_count)
    if not (0 <= moved_row < len(array) and 0 <= moved_col < len(array[0])):
        return [row[:] for row in array]
    output = [[0] * len(array[0]) for _ in array]
    for c in range(len(output[0])):
        output[moved_row][c] = color
    for r in range(len(output)):
        output[r][moved_col] = color
    return output


def solve(grid):
    return _shift_cross_by_marker(grid, 5)
