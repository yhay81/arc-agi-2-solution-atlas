def _connect_axis_markers(array, first_color, second_color, path_color):
    first = [
        (r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == first_color
    ]
    second = [
        (r, c)
        for r, row in enumerate(array)
        for c, value in enumerate(row)
        if value == second_color
    ]
    if len(first) != 1 or len(second) != 1 or first_color == second_color:
        return [row[:] for row in array]
    first_row, first_col = first[0]
    second_row, second_col = second[0]
    output = [row[:] for row in array]
    row_start, row_stop = sorted((first_col, second_col))
    for col in range(row_start, row_stop + 1):
        if output[first_row][col] == 0:
            output[first_row][col] = path_color
    row_start, row_stop = sorted((first_row, second_row))
    for row in range(row_start, row_stop + 1):
        if output[row][second_col] == 0:
            output[row][second_col] = path_color
    return output


def solve(grid):
    return _connect_axis_markers(grid, 2, 8, 4)
