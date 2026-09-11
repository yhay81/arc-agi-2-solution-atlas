def _connect_markers(array):
    output = [row[:] for row in array]
    for row in range(len(array)):
        cols = [c for c, v in enumerate(array[row]) if v != 0]
        if len(cols) == 2:
            output[row][cols[0] : cols[1] + 1] = [array[row][cols[0]]] * (cols[1] - cols[0] + 1)
    for col in range(len(array[0])):
        rows = [r for r in range(len(array)) if array[r][col] != 0]
        if len(rows) == 2:
            for r in range(rows[0], rows[1] + 1):
                output[r][col] = array[rows[0]][col]
    return output


def solve(grid):
    return _connect_markers(grid)
