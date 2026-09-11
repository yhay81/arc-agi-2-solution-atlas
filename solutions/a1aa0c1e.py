from itertools import pairwise


def _summarize_line_attached_glyphs(array):
    full_lines = [
        (row, int(line[0]))
        for row, line in enumerate(array)
        if line[0] != 0 and all(v == line[0] for v in line)
    ]
    if len(full_lines) != 4:
        return [row[:] for row in array]
    output = [[0] * 5 for _ in range(3)]
    for row in output:
        row[3] = full_lines[-1][1]
    for index, ((row, color), (next_row, _)) in enumerate(pairwise(full_lines)):
        count = sum(
            sum(v == color for v in array[glyph_row]) == 3 for glyph_row in range(row + 1, next_row)
        )
        if count > 3:
            return [row[:] for row in array]
        output[index][:count] = [color] * count
    markers = [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v == 5]
    if len(markers) != 1:
        return [row[:] for row in array]
    center_col = (len(array[0]) - 1) // 2
    distance = abs(markers[0][1] - center_col)
    marker_row = 2 - distance // 3
    if not 0 <= marker_row < 3:
        return [row[:] for row in array]
    output[marker_row][4] = 5
    return output


def solve(grid):
    return _summarize_line_attached_glyphs([row[:] for row in grid])
