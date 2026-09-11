def _fill_enclosed_with_four(array):
    output = [row[:] for row in array]
    height, width = len(array), len(array[0])
    seen = set()
    stack = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if (row in (0, height - 1) or col in (0, width - 1)) and array[row][col] == 0
    ]
    while stack:
        row, col = stack.pop()
        if (
            not (0 <= row < height and 0 <= col < width)
            or (row, col) in seen
            or array[row][col] != 0
        ):
            continue
        seen.add((row, col))
        stack.extend(((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)))
    for row in range(height):
        for col in range(width):
            if array[row][col] == 0 and (row, col) not in seen:
                output[row][col] = 4
    return output


def solve(grid):
    output = _fill_enclosed_with_four(grid)
    color_map = {0: 0, 2: 2, 4: 1}
    source = [row[:] for row in output]
    for old, new in color_map.items():
        for row in range(len(output)):
            for col in range(len(output[0])):
                if source[row][col] == old:
                    output[row][col] = new
    return output
