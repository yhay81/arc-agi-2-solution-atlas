def _crop_3x3_below_marker(array, marker=5):
    positions = [
        (r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == marker
    ]
    if len(positions) != 1:
        return [row[:] for row in array]
    row, col = positions[0]
    if row + 3 >= len(array) or col == 0 or col + 1 >= len(array[0]):
        return [row[:] for row in array]
    glyph = [line[col - 1 : col + 2] for line in array[row + 1 : row + 4]]
    colors = {value for line in glyph for value in line if value != 0}
    if len(colors) != 1 or not any(glyph):
        return [row[:] for row in array]
    occupied = [
        (r, c) for r, line in enumerate(glyph) for c, value in enumerate(line) if value != 0
    ]
    rows, cols = zip(*occupied)
    if [min(rows), min(cols)] != [0, 0] or [max(rows), max(cols)] != [2, 2]:
        return [row[:] for row in array]
    return [line[:] for line in glyph]


def solve(grid):
    return _crop_3x3_below_marker(grid)
