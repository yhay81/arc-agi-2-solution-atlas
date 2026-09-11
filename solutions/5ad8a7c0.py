def _fill_narrowest_pairs(array):
    pairs: list[tuple[int, int, int]] = []
    for row in range(len(array)):
        cols = [c for c, value in enumerate(array[row]) if value == 2]
        if len(cols) == 2:
            pairs.append((row, int(cols[0]), int(cols[1])))
    if not pairs:
        return [row[:] for row in array]
    minimum = min((right - left for _, left, right in pairs))
    if minimum <= 1:
        return [row[:] for row in array]
    output = [row[:] for row in array]
    for row, left, right in pairs:
        if right - left == minimum:
            output[row][left : right + 1] = [2] * (right - left + 1)
    return output


def solve(grid):
    return _fill_narrowest_pairs(grid)
