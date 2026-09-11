def _draw_diagonal_rays_from_single_point(array):
    positions = [(r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value != 0]
    if len(positions) != 1:
        return [row[:] for row in array]
    row, col = positions[0]
    color = array[row][col]
    output = [[0] * len(array[0]) for _ in array]
    for row_step, col_step in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        current_row, current_col = row, col
        while 0 <= current_row < len(array) and 0 <= current_col < len(array[0]):
            output[current_row][current_col] = color
            current_row += row_step
            current_col += col_step
    return output


def solve(grid):
    return _draw_diagonal_rays_from_single_point(grid)
