from collections import Counter


def solve(grid):
    a = grid
    counts = Counter(v for row in a for v in row if v)
    order = [c for c, n in counts.most_common()]
    size = max(counts.values())
    return [
        [order[min(r, c, size - 1 - r, size - 1 - c)] for c in range(size)] for r in range(size)
    ]
