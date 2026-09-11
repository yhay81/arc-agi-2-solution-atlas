from collections import Counter


def solve(grid):
    counts = Counter(v for row in grid for v in row)
    majority = min(counts, key=lambda v: (-counts[v], v))
    return [[v if v == majority else 5 for v in row] for row in grid]
