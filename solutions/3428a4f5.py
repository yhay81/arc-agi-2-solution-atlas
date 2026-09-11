def _xor_separated_panels(array):
    h, w = len(array), len(array[0])
    separator = h // 2
    if h % 2 == 0 or array[separator][0] == 0 or len(set(array[separator])) != 1:
        return array.copy()
    top, bottom = array[:separator], array[separator + 1 :]
    if len(top) != len(bottom):
        return [row[:] for row in array]
    return [
        [3 if (top[r][c] != 0) != (bottom[r][c] != 0) else 0 for c in range(w)]
        for r in range(separator)
    ]


def solve(grid):
    return _xor_separated_panels(grid)
