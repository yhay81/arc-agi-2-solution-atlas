def _fill_between_nonzero(array, color):
    output = [row[:] for row in array]
    for row in range(len(array)):
        positions = [c for c, value in enumerate(array[row]) if value != 0]
        if len(positions) >= 2:
            for col in range(positions[0], positions[-1] + 1):
                if array[row][col] == 0:
                    output[row][col] = color
    for col in range(len(array[0])):
        positions = [r for r, row in enumerate(array) if row[col] != 0]
        if len(positions) >= 2:
            for row in range(positions[0], positions[-1] + 1):
                if array[row][col] == 0:
                    output[row][col] = color
    return output


def solve(grid):
    output = _fill_between_nonzero(grid, 2)
    color_map = {0: 0, 1: 1, 2: 8}
    source = [row[:] for row in output]
    for old, new in color_map.items():
        for row in range(len(output)):
            for col in range(len(output[0])):
                if source[row][col] == old:
                    output[row][col] = new
    return output
