def _repair_rot180_marker_occlusions(array, marker_color=4):
    output = [row[:] for row in array]
    mask = [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v == marker_color]
    if not mask:
        return output
    h, w = len(array), len(array[0])
    for r, c in mask:
        output[r][c] = array[h - 1 - r][w - 1 - c]
    return output


def solve(grid):
    return _repair_rot180_marker_occlusions(grid, 4)
