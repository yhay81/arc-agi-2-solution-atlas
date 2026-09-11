from collections import Counter


def solve(grid):
    g = grid
    counts = Counter()
    for r in range(1, len(g) - 1):
        for c in range(1, len(g[0]) - 1):
            petals = [g[r + dr][c + dc] for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))]
            if g[r][c] == 4 and len(set(petals)) == 1:
                counts[petals[0]] += 1
    return [[counts.most_common(1)[0][0]]]
