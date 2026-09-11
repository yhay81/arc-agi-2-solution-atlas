def _fold_outer_frame(array):
    h, w = len(array), len(array[0])
    if h < 4 or w < 4:
        return [row[:] for row in array]
    output = [[0] * 3 for _ in range(3)]
    row_map = {0: 0, 1: 1, h - 2: 1, h - 1: 2}
    col_map = {0: 0, 1: 1, w - 2: 1, w - 1: 2}
    for source_row, target_row in row_map.items():
        for source_col, target_col in col_map.items():
            if array[source_row][source_col] != 0:
                output[target_row][target_col] = array[source_row][source_col]
    return output


def solve(grid):
    return _fold_outer_frame(grid)
