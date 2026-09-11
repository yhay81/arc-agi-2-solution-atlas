def _mark_last_row_with_top_mode(array):
    separators = [
        row for row in range(len(array)) if all(value == array[row][0] for value in array[row])
    ]
    if not separators:
        return [row[:] for row in array]
    separator = separators[0]
    region = array[:separator]
    values = [value for row in region for value in row if value != 0]
    if not len(values):
        return [row[:] for row in array]
    counts = {color: values.count(color) for color in set(values)}
    mode = max(counts, key=lambda color: (counts[color], -color))
    output = [row[:] for row in array]
    output[-1][len(array[0]) // 2] = mode
    return output


def solve(grid):
    return _mark_last_row_with_top_mode(grid)
