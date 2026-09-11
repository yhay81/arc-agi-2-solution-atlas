from math import isqrt


def _pack_frequency_squares(array):
    counts = {}
    for row in array:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    values = list(counts)
    if not values:
        return [row[:] for row in array]
    background = max(values, key=counts.get)
    items: list[tuple[int, int]] = []
    for color in values:
        count = counts[color]
        if color == background:
            continue
        side = isqrt(int(count))
        if side * side != int(count):
            return [row[:] for row in array]
        items.append((side, color))
    if not items:
        return [row[:] for row in array]
    items.sort()
    height = max((side for side, _ in items))
    width = sum((side for side, _ in items)) + len(items) - 1
    output = [[background] * width for _ in range(height)]
    left = 0
    for side, color in items:
        for r in range(height - side, height):
            for c in range(left, left + side):
                output[r][c] = color
        left += side + 1
    return output


def solve(grid):
    return _pack_frequency_squares(grid)
