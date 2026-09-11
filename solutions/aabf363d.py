from collections import Counter


def _recolor_from_single_marker(grid):
    counts = Counter(v for row in grid for v in row if v)
    values = list(counts)
    singletons = [v for v in values if counts[v] == 1]
    if len(singletons) != 1 or len(values) != 2:
        return [row[:] for row in grid]
    marker = singletons[0]
    return [[marker if value and value != marker else 0 for value in row] for row in grid]


def solve(grid):
    return _recolor_from_single_marker(grid)
