def _pack_points_by_column_snake(array):
    points = [(r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value != 0]
    if len(points) == 0 or len(points) > 9:
        return [row[:] for row in array]
    if len({col for _, col in points}) != len(points):
        return [row[:] for row in array]
    ordered = sorted(
        ((row, col, array[row][col]) for row, col in points),
        key=lambda item: item[1],
    )
    output = [[0] * 3 for _ in range(3)]
    for index, (_, _, color) in enumerate(ordered):
        out_row, offset = divmod(index, 3)
        out_col = offset if out_row % 2 == 0 else 2 - offset
        output[out_row][out_col] = color
    return output


def solve(grid):
    return _pack_points_by_column_snake(grid)
