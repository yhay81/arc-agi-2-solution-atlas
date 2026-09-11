def _expand_marker_diagonal(array, marker_color=2, object_color=3):
    markers = [
        (r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v == marker_color
    ]
    objects = [
        (r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v == object_color
    ]
    if len(markers) != 1 or len(objects) != 3:
        return [r[:] for r in array]
    marker_row, marker_col = markers[0]
    diagonal = [
        (int(row), int(col))
        for row, col in objects
        if abs(row - marker_row) == 1 and abs(col - marker_col) == 1
    ]
    if len(diagonal) != 1:
        return [r[:] for r in array]
    diagonal_row, diagonal_col = diagonal[0]
    top, left = (min(marker_row, diagonal_row), min(marker_col, diagonal_col))
    output = [[0] * (4 * (len(array[0]) - 1) + 1) for _ in range(4 * (len(array) - 1) + 1)]
    for row, col in ((marker_row, marker_col), (diagonal_row, diagonal_col)):
        target_row = top + 4 * (row - top)
        target_col = left + 4 * (col - left)
        for r in range(target_row, target_row + 4):
            for c in range(target_col, target_col + 4):
                output[r][c] = object_color
    return output


def solve(grid):
    return _expand_marker_diagonal(grid, 2, 3)
