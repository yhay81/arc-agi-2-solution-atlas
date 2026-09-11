from collections import Counter


def solve(grid):
    counts = Counter(v for row in grid for v in row if v)
    return [[color] for color in sorted(counts, key=lambda c: (-counts[c], c))]
