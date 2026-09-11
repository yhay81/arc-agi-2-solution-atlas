def _xor_separated_equal_panels(array, axis):
    h, w = len(array), len(array[0])
    lines = [
        index
        for index in range((h, w)[axis])
        if len(set([row[index] for row in array] if axis == 1 else array[index])) == 1
    ]
    for separator in lines:
        line = [row[separator] for row in array] if axis == 1 else array[separator]
        if all(v == 0 for v in line):
            continue
        if separator * 2 + 1 != (w if axis == 1 else h):
            continue
        if axis == 1:
            return [
                [
                    int((array[r][c] != 0) ^ (array[r][c + separator + 1] != 0))
                    for c in range(separator)
                ]
                for r in range(h)
            ]
        return [
            [int((array[r][c] != 0) ^ (array[r + separator + 1][c] != 0)) for c in range(w)]
            for r in range(separator)
        ]
    return [row[:] for row in array]


def solve(grid):
    return [[v * 2 for v in row] for row in _xor_separated_equal_panels(grid, 1)]
