def _connect_two_markers_cross(array):
    positions = [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v != 0]
    if len(positions) != 2:
        return [row[:] for row in array]
    (row_a, col_a), (row_b, col_b) = positions
    if row_a != row_b and col_a != col_b:
        return [row[:] for row in array]
    row, col = ((row_a + row_b) // 2, (col_a + col_b) // 2)
    if (row_a + row_b) % 2 or (col_a + col_b) % 2:
        return [row[:] for row in array]
    output = [row[:] for row in array]
    for next_row, next_col in (
        (row, col),
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1),
    ):
        if 0 <= next_row < len(output) and 0 <= next_col < len(output[0]):
            output[next_row][next_col] = 3
    return output


def solve(grid):
    return _connect_two_markers_cross(grid)
