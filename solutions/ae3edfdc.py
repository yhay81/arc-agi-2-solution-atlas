def _project_distant_markers_around_centers(array):
    output = [[0] * len(array[0]) for _ in array]
    for center_color, marker_color in ((1, 7), (2, 3)):
        centers = [
            (r, c)
            for r, row in enumerate(array)
            for c, value in enumerate(row)
            if value == center_color
        ]
        markers = [
            (r, c)
            for r, row in enumerate(array)
            for c, value in enumerate(row)
            if value == marker_color
        ]
        if len(centers) != 1 or not len(markers):
            continue
        row, col = centers[0]
        output[row][col] = center_color
        for marker_row, marker_col in markers:
            row_delta = (marker_row > row) - (marker_row < row)
            col_delta = (marker_col > col) - (marker_col < col)
            if row_delta and 0 <= row + row_delta < len(array):
                output[row + row_delta][col] = marker_color
            if col_delta and 0 <= col + col_delta < len(array[0]):
                output[row][col + col_delta] = marker_color
    return output


def solve(grid):
    return _project_distant_markers_around_centers(grid)
