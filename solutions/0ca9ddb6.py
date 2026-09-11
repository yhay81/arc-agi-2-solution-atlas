def _stamp_marker_patterns(array):
    output = [row[:] for row in array]
    h, w = len(array), len(array[0])
    for row, rowdata in enumerate(array):
        for col, value in enumerate(rowdata):
            if value != 1:
                continue
            for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                target_row, target_col = (row + delta_row, col + delta_col)
                if (
                    0 <= target_row < h
                    and 0 <= target_col < w
                    and output[target_row][target_col] == 0
                ):
                    output[target_row][target_col] = 7
    for row, rowdata in enumerate(array):
        for col, value in enumerate(rowdata):
            if value != 2:
                continue
            for delta_row, delta_col in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                target_row, target_col = (row + delta_row, col + delta_col)
                if (
                    0 <= target_row < h
                    and 0 <= target_col < w
                    and output[target_row][target_col] == 0
                ):
                    output[target_row][target_col] = 4
    return output


def solve(grid):
    return _stamp_marker_patterns([row[:] for row in grid])
