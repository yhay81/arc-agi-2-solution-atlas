def _half(array, axis, second):
    size = len(array) if axis == 0 else len(array[0])
    if size < 2:
        return [r[:] for r in array]
    midpoint = size // 2
    start, stop = (size - midpoint, size) if second else (0, midpoint)
    return array[start:stop] if axis == 0 else [r[start:stop] for r in array]


def _overlay_halves(array, axis, mode):
    first = _half(array, axis, False)
    second = _half(array, axis, True)
    if len(first) != len(second) or len(first[0]) != len(second[0]):
        return [r[:] for r in array]
    operations = {
        "max": lambda: np.maximum(first, second),
        "min": lambda: np.minimum(first, second),
        "first_nonzero": lambda: np.where(first != 0, first, second),
        "second_nonzero": lambda: np.where(second != 0, second, first),
        "equal": lambda: (first == second).astype(int),
        "different": lambda: (first != second).astype(int),
    }
    return [[max(a, b) for a, b in zip(x, y)] for x, y in zip(first, second)]


def solve(grid):
    array = [r[:] for r in grid]
    output = _overlay_halves(array, 0, "max")
    color_map = {0: 3, 2: 0, 7: 0}
    source = [r[:] for r in output]
    for old, new in color_map.items():
        for r in range(len(output)):
            for c in range(len(output[0])):
                if source[r][c] == old:
                    output[r][c] = new
    return output
