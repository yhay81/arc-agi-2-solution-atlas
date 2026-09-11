def _fill_center_marker_glyph(array, marker=8):
    positions = [
        (r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == marker
    ]
    if len(positions) != 1:
        return [row[:] for row in array]
    row, col = positions[0]
    if row == 0 or col == 0 or row == len(array) - 1 or col == len(array[0]) - 1:
        return [row[:] for row in array]
    glyph = [line[col - 1 : col + 2] for line in array[row - 1 : row + 2]]
    colors = {value for line in glyph for value in line if value not in (0, marker)}
    if len(colors) != 1:
        return [row[:] for row in array]
    glyph[1][1] = next(iter(colors))
    return glyph


def solve(grid):
    return _fill_center_marker_glyph(grid)
