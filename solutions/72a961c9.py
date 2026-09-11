def _build_marker_towers(array):
    output = [row[:] for row in array]
    for row in range(len(array)):
        if sum(value == 1 for value in array[row]) < max(1, len(array[0]) // 2):
            continue
        for col, value in enumerate(array[row]):
            if value == 8 and row >= 3:
                output[row - 3][col] = 8
                for r in range(row - 2, row):
                    output[r][col] = 1
            elif value == 2 and row >= 4:
                output[row - 4][col] = 2
                for r in range(row - 3, row):
                    output[r][col] = 1
    return output


def solve(grid):
    return _build_marker_towers(grid)
