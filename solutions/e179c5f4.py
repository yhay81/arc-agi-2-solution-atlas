def _bouncing_diagonal(array):
    height, width = len(array), len(array[0])
    output = [[8] * width for _ in range(height)]
    col, direction = (0, 1)
    for row in range(height - 1, -1, -1):
        output[row][col] = 1
        if width > 1 and (col + direction < 0 or col + direction >= width):
            direction *= -1
        col += direction
    return output


def solve(grid):
    return _bouncing_diagonal(grid)
