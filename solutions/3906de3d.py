def _gravity_axis(array, axis, reverse):
    h, w = len(array), len(array[0])
    output = [[0] * w for _ in range(h)]
    count = w if axis == 0 else h
    for index in range(count):
        line = [array[r][index] for r in range(h)] if axis == 0 else array[index]
        values = [v for v in line if v != 0]
        if reverse:
            values = values[::-1]
        target = [0] * len(line)
        if reverse:
            if len(values):
                target[-len(values) :] = values
        elif len(values):
            target[: len(values)] = values
        if axis == 0:
            for r, v in enumerate(target):
                output[r][index] = v
        else:
            output[index] = target
    return output


def solve(grid):
    return _gravity_axis(grid, 0, False)
