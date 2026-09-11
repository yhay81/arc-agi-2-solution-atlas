def _xor_equal_panels(array, axis):
    if axis != 0 or len(array) % 2:
        return [row[:] for row in array]
    half = len(array) // 2
    return [
        [int((a != 0) ^ (b != 0)) for a, b in zip(array[r], array[r + half])] for r in range(half)
    ]


def solve(grid):
    array = [row[:] for row in grid]
    output = _xor_equal_panels(array, 0)
    color_map = {1: 6, 0: 0}
    return [[color_map[v] for v in row] for row in output]
