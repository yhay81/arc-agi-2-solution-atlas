def _cross_connect_8_7(array):
    eight = [(r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == 8]
    seven = [(r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == 7]
    if len(eight) != 1 or len(seven) != 1:
        return [row[:] for row in array]
    row_8, col_8 = eight[0]
    row_7, col_7 = seven[0]
    output = [row[:] for row in array]
    for row in output:
        row[col_8] = 8
        row[col_7] = 7
    output[row_8] = [8] * len(array[0])
    output[row_7] = [7] * len(array[0])
    output[row_8][col_7] = 2
    output[row_7][col_8] = 2
    return output


def solve(grid):
    return _cross_connect_8_7(grid)
