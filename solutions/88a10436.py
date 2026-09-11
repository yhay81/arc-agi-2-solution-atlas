def _stamp_glyph_centered_on_five(array):
    markers = [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v == 5]
    if len(markers) != 1:
        return [r[:] for r in array]
    glyph_positions = [
        (r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v not in (0, 5)
    ]
    if not len(glyph_positions):
        return [r[:] for r in array]
    top, left = min(r for r, c in glyph_positions), min(c for r, c in glyph_positions)
    bottom, right = max(r for r, c in glyph_positions), max(c for r, c in glyph_positions)
    glyph = [r[left : right + 1] for r in array[top : bottom + 1]]
    gh, gw = len(glyph), len(glyph[0])
    if glyph[gh // 2][gw // 2] == 0:
        return [r[:] for r in array]
    marker_row, marker_col = markers[0]
    target_top = marker_row - gh // 2
    target_left = marker_col - gw // 2
    if (
        target_top < 0
        or target_left < 0
        or target_top + gh > len(array)
        or target_left + gw > len(array[0])
    ):
        return [r[:] for r in array]
    output = [r[:] for r in array]
    for r in range(gh):
        for c in range(gw):
            if glyph[r][c] != 0:
                output[target_top + r][target_left + c] = glyph[r][c]
    return output


def solve(grid):
    return _stamp_glyph_centered_on_five([r[:] for r in grid])
