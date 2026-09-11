def _crop_symmetric_6x6(array):
    positions = [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v != 0]
    if not len(positions):
        return [row[:] for row in array]
    top = min(r for r, c in positions)
    left = min(c for r, c in positions)
    bottom = max(r for r, c in positions)
    right = max(c for r, c in positions)
    if (bottom - top + 1, right - left + 1) != (6, 6):
        return [row[:] for row in array]
    return [row[left : left + 3] for row in array[top : top + 3]]


def solve(grid):
    return _crop_symmetric_6x6(grid)
