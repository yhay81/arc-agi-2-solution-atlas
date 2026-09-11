from collections import Counter


def solve(grid):
    a = grid
    counts = Counter(v for row in a for v in row)
    if len(set(counts.values())) != len(counts):
        raise ValueError("Tied color frequencies are not identified by training")
    stream = [color for color, count in counts.most_common() for _ in range(count)]
    out = [[0] * len(a[0]) for _ in a]
    index = 0
    for c in range(len(a[0])):
        for r in reversed(range(len(a))):
            out[r][c] = stream[index]
            index += 1
    return out
