def _scale_nested_rings_by_two(array):
    height, width = len(array), len(array[0])
    if height != width or height < 2:
        return [row[:] for row in array]
    ring_colors: list[int] = []
    for ring in range(height):
        values = {
            array[row][col]
            for row in range(height)
            for col in range(width)
            if max(row, col) == ring and array[row][col] != 0
        }
        if len(values) > 1:
            return [row[:] for row in array]
        ring_colors.append(next(iter(values), 0))
    nonempty = [index for index, color in enumerate(ring_colors) if color != 0]
    if not nonempty:
        return [row[:] for row in array]
    period = nonempty[-1] + 1
    return [
        [ring_colors[max(row, col) % period] for col in range(2 * width)]
        for row in range(2 * height)
    ]


def solve(grid):
    return _scale_nested_rings_by_two(grid)
