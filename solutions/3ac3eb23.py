def _repeat_top_markers_as_diagonal_stripes(array):
    if len(array) < 2 or any(value != 0 for row in array[1:] for value in row):
        return [row[:] for row in array]
    top = array[0]
    if not any(top):
        return [row[:] for row in array]
    output = [[0] * len(top) for _ in array]
    for row in range(0, len(array), 2):
        output[row] = top[:]
    for col, color in enumerate(top):
        if not color:
            continue
        if col > 0:
            for row in range(1, len(array), 2):
                output[row][col - 1] = color
        if col + 1 < len(top):
            for row in range(1, len(array), 2):
                output[row][col + 1] = color
    return output


def solve(grid):
    return _repeat_top_markers_as_diagonal_stripes(grid)
