from collections import Counter


def solve(grid):
    a = grid
    tiles = [
        tuple(tuple(row[c : c + 5]) for row in a[r : r + 5])
        for r in range(0, len(a), 6)
        for c in range(0, len(a[0]), 6)
    ]
    counts = Counter(tiles)
    common = max(counts, key=counts.get)
    rare = min(counts, key=counts.get)
    return [[common[r][c] if common[r][c] == rare[r][c] else 1 for c in range(5)] for r in range(5)]
