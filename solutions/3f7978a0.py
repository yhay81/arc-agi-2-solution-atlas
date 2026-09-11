def _crop_vertical_frame_with_margin(array, frame_color=5):
    positions = [
        (r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v == frame_color
    ]
    if not len(positions):
        return [row[:] for row in array]
    top, left = min(positions)
    bottom, right = max(positions)
    top = max(0, top - 1)
    bottom = min(len(array) - 1, bottom + 1)
    return [row[left : right + 1] for row in array[top : bottom + 1]]


def solve(grid):
    return _crop_vertical_frame_with_margin(grid, 5)
