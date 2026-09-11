def _checker_two_rows(array):
    if len(array) < 2:
        return [row[:] for row in array]
    return [
        [array[(row + col) % 2][0] for col in range(len(array[0]))] for row in range(len(array))
    ]


def solve(grid):
    return _checker_two_rows(grid)
