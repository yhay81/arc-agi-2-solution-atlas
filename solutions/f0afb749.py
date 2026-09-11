def _scale_cells_with_diagonal_rays(array):
    height, width = len(array), len(array[0])
    output = [[0] * (2 * width) for _ in range(2 * height)]
    for row in range(height):
        for col in range(width):
            color = array[row][col]
            if color == 0:
                continue
            for rr in range(2 * row, 2 * row + 2):
                for cc in range(2 * col, 2 * col + 2):
                    output[rr][cc] = color
            for step in range(-min(row, col), min(height - row, width - col)):
                ray_row, ray_col = (row + step, col + step)
                top, left = (2 * ray_row, 2 * ray_col)
                for delta in (0, 1):
                    target_row, target_col = (top + delta, left + delta)
                    if output[target_row][target_col] == 0:
                        output[target_row][target_col] = 1
    return output


def solve(grid):
    return _scale_cells_with_diagonal_rays(grid)
