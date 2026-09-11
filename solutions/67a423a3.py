def _fill_cross_center_3x3(array):
    full_rows = [row for row in range(len(array)) if all(value != 0 for value in array[row])]
    full_cols = [col for col in range(len(array[0])) if all(row[col] != 0 for row in array)]
    if len(full_rows) != 1 or len(full_cols) != 1:
        return [row[:] for row in array]
    center_row, center_col = (full_rows[0], full_cols[0])
    if not (1 <= center_row < len(array) - 1 and 1 <= center_col < len(array[0]) - 1):
        return [row[:] for row in array]
    output = [row[:] for row in array]
    region = [[4] * 3 for _ in range(3)]
    region[1][1] = array[center_row][center_col]
    for r in range(3):
        output[center_row - 1 + r][center_col - 1 : center_col + 2] = region[r]
    return output


def solve(grid):
    return _fill_cross_center_3x3(grid)
