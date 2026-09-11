def _crop_non_background(array):
    values = [v for row in array for v in row]
    background = max(set(values), key=values.count)
    positions = [
        (r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v != background
    ]
    if not len(positions):
        return [row[:] for row in array]
    top = min(r for r, _ in positions)
    left = min(c for _, c in positions)
    bottom = max(r for r, _ in positions)
    right = max(c for _, c in positions)
    return [row[left : right + 1] for row in array[top : bottom + 1]]


def _crop_swap_two_colors(array):
    cropped = _crop_non_background(array)
    colors = sorted({v for row in cropped for v in row if v != 0})
    if len(colors) != 2:
        return [row[:] for row in array]
    output = [row[:] for row in cropped]
    first, second = colors
    for r, row in enumerate(cropped):
        for c, v in enumerate(row):
            if v == first:
                output[r][c] = second
            elif v == second:
                output[r][c] = first
    return output


def solve(grid):
    return _crop_swap_two_colors(grid)
