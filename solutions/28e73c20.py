def _draw_square_spiral(array):
    height, width = len(array), len(array[0])
    if height != width or height < 3 or any(v for row in array for v in row):
        return [row[:] for row in array]
    output = [[0] * width for _ in array]
    for layer in range(0, height // 2 + 1, 2):
        top, left = (layer, layer)
        right, bottom = (height - 1 - layer, width - 1 - layer)
        if top > bottom or left > right:
            continue
        for col in range(max(0, layer - 2), right + 1):
            output[top][col] = 3
        for row in range(top, bottom + 1):
            output[row][right] = 3
        for col in range(left, right + 1):
            output[bottom][col] = 3
        for row in range(top + 2, bottom + 1):
            output[row][left] = 3
    if height % 4 == 0:
        output[height // 2][height // 2 - 1] = 3
    return output


def solve(grid):
    return _draw_square_spiral(grid)
