from collections import Counter


def mode(values):
    return Counter(v for row in values for v in row).most_common(1)[0][0]


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    bg = mode(a)
    start = next(i for i, row in enumerate(a) if any(v != bg for v in row))
    p = a[start:]
    return [p[(r - start) % len(p)][:] for r in range(len(a))]
