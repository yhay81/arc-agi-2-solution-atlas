def _half(array, axis, second):
    size = len(array) if axis == 0 else len(array[0])
    if size < 2:
        return [row[:] for row in array]
    midpoint = size // 2
    start, stop = (size - midpoint, size) if second else (0, midpoint)
    return (
        [row[:] for row in array[start:stop]] if axis == 0 else [row[start:stop] for row in array]
    )


def _overlay_halves_mapped(array, axis, fill, second_map):
    first = _half(array, axis, False)
    second = _half(array, axis, True)
    if (len(first), len(first[0])) != (len(second), len(second[0])):
        return [row[:] for row in array]
    mapped = [row[:] for row in second]
    for old, new in second_map.items():
        for r in range(len(mapped)):
            for c in range(len(mapped[0])):
                if second[r][c] == int(old):
                    mapped[r][c] = int(new)
    output = [[fill] * len(first[0]) for _ in first]
    for r in range(len(first)):
        for c in range(len(first[0])):
            output[r][c] = (
                first[r][c] if first[r][c] != 0 else mapped[r][c] if second[r][c] != 0 else fill
            )
    return output


def solve(grid):
    return _overlay_halves_mapped(grid, 0, 0, {"7": 7})
