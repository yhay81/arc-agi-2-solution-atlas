def _project_alternating_stripes_from_bottom_marker(array):
    occupied = [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v != 0]
    if len(occupied) != 1:
        return [row[:] for row in array]
    marker_row, marker_col = occupied[0]
    if marker_row != len(array) - 1:
        return [row[:] for row in array]
    marker_color = array[marker_row][marker_col]
    output = [[0] * len(array[0]) for _ in array]
    stripe_cols = list(range(marker_col, len(array[0]), 2))
    for col in stripe_cols:
        for row in range(len(array)):
            output[row][col] = marker_color
    for index, col in enumerate(stripe_cols):
        if col + 1 < len(array[0]):
            edge_row = 0 if index % 2 == 0 else len(array) - 1
            output[edge_row][col + 1] = 5
    return output


def solve(grid):
    return _project_alternating_stripes_from_bottom_marker(grid)
