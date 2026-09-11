def _stamp_pattern_count(array):
    count = sum(value != 0 for row in array for value in row)
    factor = 9 - count
    if count <= 0 or factor <= 0 or count > factor * factor:
        return [row[:] for row in array]
    height, width = len(array), len(array[0])
    output = [[0] * (width * factor) for _ in range(height * factor)]
    for index in range(count):
        row, col = divmod(index, factor)
        for r in range(height):
            output[row * height + r][col * width : (col + 1) * width] = array[r]
    return output


def solve(grid):
    return _stamp_pattern_count(grid)
