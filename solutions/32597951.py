def _recolor_one_inside_eight_bbox(array):
    markers = [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v == 8]
    if not len(markers):
        return [row[:] for row in array]
    top = min(r for r, c in markers)
    left = min(c for r, c in markers)
    bottom = max(r for r, c in markers)
    right = max(c for r, c in markers)
    output = [row[:] for row in array]
    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            if output[r][c] == 1:
                output[r][c] = 3
    return output


def solve(grid):
    return _recolor_one_inside_eight_bbox(grid)
