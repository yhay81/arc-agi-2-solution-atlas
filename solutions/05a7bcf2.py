def _transpose(grid):
    return [list(column) for column in zip(*grid)]


def _find_divider(grid):
    height, width = len(grid), len(grid[0])
    for col in range(width):
        if sum(grid[row][col] == 8 for row in range(height)) > 0.8 * height:
            return True, col
    for row in range(height):
        if sum(value == 8 for value in grid[row]) > 0.8 * width:
            return False, row
    positions = [(row, col) for row in range(height) for col in range(width) if grid[row][col] == 8]
    return False, positions[0][0] if positions else height // 2


def _move_histogram(source, result, divider):
    objects = [col for col, value in enumerate(result) if value == 3]
    if not objects:
        return result
    if min(objects) >= divider:
        return _move_histogram(source[::-1], result[::-1], len(result) - 1 - divider)[::-1]

    for col in range(max(objects) + 1, divider):
        result[col] = 4
    histogram_start = None
    for col in range(divider + 1, len(source)):
        if source[col] == 2:
            histogram_start = col
            break
        result[col] = 8
    if histogram_start is None:
        return result

    histogram_end = histogram_start
    while histogram_end < len(source) and source[histogram_end] == 2:
        histogram_end += 1
    length = histogram_end - histogram_start
    destination = len(source) - length
    for col in range(histogram_start, histogram_end):
        result[col] = 0
    for col in range(destination, len(source)):
        result[col] = 2
    for col in range(histogram_start, destination):
        result[col] = 8
    return result


def solve(grid):
    vertical, divider = _find_divider(grid)
    source = [row[:] for row in grid] if vertical else _transpose(grid)
    result = [[3 if value == 4 else value for value in row] for row in source]
    result = [_move_histogram(row, output, divider) for row, output in zip(source, result)]
    return result if vertical else _transpose(result)
