def _growing_rows(array):
    if len(array) != 1:
        return [row[:] for row in array]
    color = array[0][0]
    initial = sum(v == color for v in array[0])
    output = [[0] * len(array[0]) for _ in range(len(array[0]) // 2)]
    for row in range(len(output)):
        for col in range(min(initial + row, len(output[0]))):
            output[row][col] = color
    return output


def solve(grid):
    return _growing_rows(grid)
