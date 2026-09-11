def _center_line_from_count(array):
    counts = {}
    for row in array:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    if len(counts) != 2:
        return [row[:] for row in array]
    values = sorted(counts)
    background = max(values, key=lambda value: counts[value])
    foreground = min(values, key=lambda value: counts[value])
    length = min(counts.values())
    output = [[background] * len(array[0]) for _ in array]
    row = len(array) // 2
    left = max(0, (len(array[0]) - length) // 2)
    right = min(len(array[0]), left + length)
    output[row][left:right] = [foreground] * (right - left)
    return output


def solve(grid):
    return _center_line_from_count(grid)
