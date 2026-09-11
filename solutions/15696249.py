def _tile_by_constant_line(array):
    if len(array) != len(array[0]) or len(array) < 2:
        return [row[:] for row in array]
    size = len(array)
    constant_rows = [
        row for row in range(size) if all(value == array[row][0] for value in array[row])
    ]
    constant_cols = [
        col for col in range(size) if all(array[row][col] == array[0][col] for row in range(size))
    ]
    output = [[0] * (size * size) for _ in range(size * size)]
    if constant_rows:
        row = constant_rows[0]
        for r in range(size):
            output[row * size + r] = array[r] * size
        return output
    if constant_cols:
        col = constant_cols[0]
        for block in range(size):
            for r in range(size):
                output[block * size + r][col * size : (col + 1) * size] = array[r]
        return output
    return [row[:] for row in array]


def solve(grid):
    return _tile_by_constant_line(grid)
