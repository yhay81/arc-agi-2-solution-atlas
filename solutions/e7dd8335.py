def _recolor_lower_half(array, source_color=1, target_color=2):
    positions = [
        (r, c)
        for r, row in enumerate(array)
        for c, value in enumerate(row)
        if value == source_color
    ]
    if not len(positions):
        return [row[:] for row in array]
    top = min(r for r, _ in positions)
    bottom = max(r for r, _ in positions)
    split = (top + bottom + 1) // 2
    output = [row[:] for row in array]
    for r, c in positions:
        if r >= split:
            output[r][c] = target_color
    return output


def solve(grid):
    return _recolor_lower_half(grid, 1, 2)
