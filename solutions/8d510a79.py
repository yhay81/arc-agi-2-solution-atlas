def _extend_one_away_two_toward_separator(array):
    separators = [
        row
        for row in range(len(array))
        if array[row][0] != 0 and all(value == array[row][0] for value in array[row])
    ]
    if len(separators) != 1:
        return [row[:] for row in array]
    separator = separators[0]
    output = [row[:] for row in array]
    markers = [
        (row, col, array[row][col])
        for row in range(len(array))
        for col in range(len(array[0]))
        if array[row][col] in (1, 2)
    ]
    for row, col, color in markers:
        if row < separator:
            start, stop = (0, row) if color == 1 else (row, separator - 1)
        elif row > separator:
            start, stop = (row, len(array) - 1) if color == 1 else (separator + 1, row)
        else:
            continue
        for r in range(start, stop + 1):
            output[r][col] = color
    return output


def solve(grid):
    return _extend_one_away_two_toward_separator(grid)
