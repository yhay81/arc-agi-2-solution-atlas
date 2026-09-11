def _fill_marker_row_column_intersections(array, marker_color=5, fill_color=2):
    if len(array) < 2 or len(array[0]) < 2:
        return [row[:] for row in array]
    marker = marker_color
    active_cols = [col for col, value in enumerate(array[0][:-1]) if value == marker]
    active_rows = [row for row in range(1, len(array)) if array[row][-1] == marker]
    if not active_cols or not active_rows:
        return [row[:] for row in array]
    for row in range(len(array)):
        for col in range(len(array[0])):
            allowed = row == 0 or col == len(array[0]) - 1
            if (not allowed and array[row][col] != 0) or (
                allowed and array[row][col] not in (0, marker)
            ):
                return [item[:] for item in array]
    output = [row[:] for row in array]
    for row in active_rows:
        for col in active_cols:
            output[row][col] = fill_color
    return output


def solve(grid):
    return _fill_marker_row_column_intersections(grid, 5, 2)
