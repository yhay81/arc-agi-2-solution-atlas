from collections import Counter


def _crop_non_background(grid):
    background = Counter(v for row in grid for v in row).most_common(1)[0][0]
    positions = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v != background]
    if not len(positions):
        return [row[:] for row in grid]
    top, left = min(r for r, c in positions), min(c for r, c in positions)
    bottom, right = max(r for r, c in positions), max(c for r, c in positions)
    return [row[left : right + 1] for row in grid[top : bottom + 1]]


def solve(grid):
    return [row[::-1] for row in _crop_non_background(grid)]
