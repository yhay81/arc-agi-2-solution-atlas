from collections import Counter


def solve(grid):
    g = grid
    out = []
    for row in g:
        color = Counter(v for v in row if v not in (0, 7)).most_common(1)[0][0]
        out.append([0 if v == color else color for v in row])
    return out
