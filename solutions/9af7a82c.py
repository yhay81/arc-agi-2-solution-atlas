from collections import Counter


def _color_histogram(array):
    counts = Counter(v for row in array for v in row if v != 0)
    values = list(counts)
    if not len(values):
        return [row[:] for row in array]
    ordered = sorted(((v, counts[v]) for v in values), key=lambda item: -item[1])
    output = [[0] * len(ordered) for _ in range(ordered[0][1])]
    for col, (color, count) in enumerate(ordered):
        for row in range(count):
            output[row][col] = color
    return output


def solve(grid):
    return _color_histogram(grid)
