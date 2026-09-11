def _fill_down(array):
    output = [row[:] for row in array]
    for col in range(len(output[0])):
        current = 0
        for row in range(len(output)):
            if output[row][col] != 0:
                current = output[row][col]
            elif current:
                output[row][col] = current
    return output


def solve(grid):
    return _fill_down(grid)
