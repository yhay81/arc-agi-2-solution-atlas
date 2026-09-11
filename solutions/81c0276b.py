from collections import Counter


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    separators = {row[0] for row in g if len(set(row)) == 1 and row[0] != 0}
    if len(separators) != 1:
        raise ValueError("Expected one separator color")
    sep = separators.pop()
    counts = Counter(v for row in g for v in row if v not in (0, sep))
    counts = {v: n // 4 for v, n in counts.items()}
    width = max(counts.values())
    return [[v] * n + [0] * (width - n) for v, n in sorted(counts.items(), key=lambda p: p[1])]
