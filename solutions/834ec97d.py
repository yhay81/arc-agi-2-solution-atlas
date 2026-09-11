def _move_marker_down_stripes(array):
    positions = [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v]
    if len(positions) != 1:
        return [row[:] for row in array]
    row, col = positions[0]
    if row + 1 >= len(array):
        return [r[:] for r in array]
    output = [[0] * len(array[0]) for _ in array]
    for r in range(row + 1):
        for c in range(len(array[0])):
            if (c - col) % 2 == 0:
                output[r][c] = 4
    output[row + 1][col] = array[row][col]
    return output


def solve(grid):
    return _move_marker_down_stripes(grid)
