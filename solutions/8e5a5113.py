def _rot(a):
    return [list(x) for x in zip(*a)][::-1]


def _fill_rotation_panels(array):
    separators = [c for c in range(len(array[0])) if all(row[c] == 5 for row in array)]
    if len(separators) != 2:
        return [row[:] for row in array]
    first = [row[: separators[0]] for row in array]
    if len(first) != len(first[0]):
        return [row[:] for row in array]
    output = [row[:] for row in array]
    r3 = _rot(_rot(_rot(first)))
    r2 = _rot(_rot(first))
    for r in range(len(array)):
        output[r][separators[0] + 1 : separators[1]] = r3[r]
        output[r][separators[1] + 1 :] = r2[r]
    return output


def solve(grid):
    return _fill_rotation_panels(grid)
