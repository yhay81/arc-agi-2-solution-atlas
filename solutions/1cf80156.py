from collections import Counter


def _crop_non_background(array):
    counts = Counter(value for row in array for value in row)
    background = min(counts, key=lambda value: (-counts[value], value))
    positions = [
        (r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value != background
    ]
    if not len(positions):
        return [row[:] for row in array]
    top, left = min(r for r, _ in positions), min(c for _, c in positions)
    bottom, right = max(r for r, _ in positions), max(c for _, c in positions)
    return [row[left : right + 1] for row in array[top : bottom + 1]]


def solve(grid):
    return _crop_non_background(grid)
