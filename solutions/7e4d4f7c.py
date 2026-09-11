from collections import Counter


def solve(grid):
    a = grid
    bg = Counter(v for row in a for v in row).most_common(1)[0][0]
    return [a[0][:], a[1][:], [6 if v != bg else bg for v in a[0]]]
