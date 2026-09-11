def _alternate_right_from_markers(array):
    output = [row[:] for row in array]
    for row in range(len(array)):
        positions = [c for c, value in enumerate(array[row]) if value != 0]
        if len(positions) != 1:
            continue
        col = positions[0]
        color = array[row][col]
        for target in range(col + 1, len(array[row])):
            output[row][target] = color if (target - col) % 2 == 0 else 5
    return output


def solve(grid):
    return _alternate_right_from_markers(grid)
