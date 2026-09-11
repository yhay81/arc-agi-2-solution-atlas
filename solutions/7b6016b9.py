def _fill_enclosed_with_four(array):
    output = [row[:] for row in array]
    height, width = len(array), len(array[0])
    seen = [[False] * width for _ in range(height)]
    stack = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if (row in (0, height - 1) or col in (0, width - 1)) and array[row][col] == 0
    ]
    while stack:
        row, col = stack.pop()
        if not (0 <= row < height and 0 <= col < width) or seen[row][col] or array[row][col] != 0:
            continue
        seen[row][col] = True
        stack.extend(((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)))
    for row in range(height):
        for col in range(width):
            if array[row][col] == 0 and not seen[row][col]:
                output[row][col] = 4
    return output


def _fill_enclosed_color(array, color):
    output = _fill_enclosed_with_four(array)
    for row in range(len(array)):
        for col in range(len(array[0])):
            if array[row][col] == 0 and output[row][col] == 4:
                output[row][col] = color
    return output


def solve(grid):
    array = [row[:] for row in grid]
    output = _fill_enclosed_color(array, 2)
    color_map = {0: 3, 1: 1, 2: 2, 8: 8, 4: 4}
    source = [row[:] for row in output]
    for old, new in color_map.items():
        for row in range(len(output)):
            for col in range(len(output[0])):
                if source[row][col] == old:
                    output[row][col] = new
    return output
