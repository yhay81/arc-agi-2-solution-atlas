from collections import Counter


def solve(grid):
    a = grid
    counts = Counter(value for row in a for value in row)
    colors = [c for c, n in counts.most_common(2)]
    return [[value if value in colors else 7 for value in row] for row in a]
