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
            for r in range(h):
                output[r][index] = target[r]
        else:
            output[index] = target
    return output


def _sort_lines(array, axis, reverse):
    h, w = len(array), len(array[0])
    counts = (
        [sum(v != 0 for v in array[r]) for r in range(h)]
        if axis == 0
        else [sum(array[r][c] != 0 for r in range(h)) for c in range(w)]
    )
    order = sorted(range(len(counts)), key=counts.__getitem__, reverse=reverse)
    if reverse:
        order = order[::-1]
    return (
        [array[r][:] for r in order]
        if axis == 0
        else [[array[r][c] for c in order] for r in range(h)]
    )


def solve(grid):
    output = _sort_lines(grid, 0, False)
    output = _gravity_axis(output, 1, True)
    return output
