def _fill_columns_to_bottom_marker(array, marker_color=5):
    output = [row[:] for row in array]
    for col in range(len(array[0])):
        if array[-1][col] != marker_color:
            continue
        current = marker_color
        for row in range(len(array) - 1, -1, -1):
            value = array[row][col]
            if value != 0:
                current = value
            else:
                output[row][col] = current
    return output


def solve(grid):
    return _fill_columns_to_bottom_marker(grid, 5)
