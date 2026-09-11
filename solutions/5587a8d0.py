def _frequency_concentric_frames(array):
    counts = {}
    for row in array:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    values = list(counts)
    if len(values) < 2:
        return [row[:] for row in array]
    background = max(values, key=counts.get)
    ordered = sorted(
        ((value, counts[value]) for value in values if value != background),
        key=lambda item: (-item[1], item[0]),
    )
    if not ordered:
        return [row[:] for row in array]
    size = 2 * len(ordered) - 1
    output = [[0] * size for _ in range(size)]
    for layer, (color, _) in enumerate(ordered):
        top, left = (layer, layer)
        bottom, right = (size - 1 - layer, size - 1 - layer)
        for c in range(left, right + 1):
            output[top][c] = output[bottom][c] = color
        for r in range(top, bottom + 1):
            output[r][left] = output[r][right] = color
    return output


def solve(grid):
    return _frequency_concentric_frames(grid)
