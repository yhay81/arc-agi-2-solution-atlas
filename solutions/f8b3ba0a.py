def _remove_uniform_lines(array):
    rows = [len(set(row)) != 1 for row in array]
    cols = [len({array[r][c] for r in range(len(array))}) != 1 for c in range(len(array[0]))]
    if not any(rows) or not any(cols):
        return [row[:] for row in array]
    return [
        [array[r][c] for c, keep in enumerate(cols) if keep] for r, keep in enumerate(rows) if keep
    ]


def _non_background_colors_by_frequency(array):
    compact = _remove_uniform_lines(array)
    values = sorted({value for row in compact for value in row})
    if not len(values):
        return [row[:] for row in array]
    background = max(values, key=lambda v: sum(row.count(v) for row in compact))
    colors = [value for value in values if value != background]
    ranked = sorted(colors, key=lambda color: (-sum(row.count(color) for row in compact), color))
    return [[color] for color in ranked]


def solve(grid):
    return _non_background_colors_by_frequency(grid)
