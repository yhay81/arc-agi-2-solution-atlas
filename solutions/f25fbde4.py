from collections import Counter


def _crop_non_background(array):
    counts = Counter(v for row in array for v in row)
    background = min(counts, key=lambda v: (-counts[v], v))
    positions = [
        (r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v != background
    ]
    if not len(positions):
        return [row[:] for row in array]
    top = min(r for r, c in positions)
    left = min(c for r, c in positions)
    bottom = max(r for r, c in positions)
    right = max(c for r, c in positions)
    return [row[left : right + 1] for row in array[top : bottom + 1]]


def solve(grid):
    output = _crop_non_background(grid)
    return [[v for v in row for _ in (0, 1)] for row in output for _ in (0, 1)]
