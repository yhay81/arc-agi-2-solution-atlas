def _crop_between_marker_corners(array):
    colors = sorted({value for row in array for value in row if value != 0})
    for color in colors:
        points = [
            (r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == color
        ]
        if len(points) != 4:
            continue
        rows = sorted({row for row, _ in points})
        cols = sorted({col for _, col in points})
        if len(rows) != 2 or len(cols) != 2:
            continue
        corners = {(rows[0], cols[0]), (rows[0], cols[1]), (rows[1], cols[0]), (rows[1], cols[1])}
        if set(points) != corners or rows[1] - rows[0] <= 1 or cols[1] - cols[0] <= 1:
            continue
        interior = [row[cols[0] + 1 : cols[1]] for row in array[rows[0] + 1 : rows[1]]]
        return [[color if value != 0 else 0 for value in row] for row in interior]
    return [row[:] for row in array]


def solve(grid):
    return _crop_between_marker_corners(grid)
