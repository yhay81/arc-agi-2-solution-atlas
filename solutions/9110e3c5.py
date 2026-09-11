from collections import Counter


def dominant_color(grid):
    counts = Counter(v for row in grid for v in row)
    maximum = max(counts[c] for c in (1, 2, 3))
    winners = [c for c in (1, 2, 3) if counts[c] == maximum]
    if maximum == 0 or len(winners) != 1:
        raise ValueError("A unique most frequent blue/red/green color is required")
    return winners[0]


def solve(grid):
    prototypes = {
        1: [[0, 0, 8], [8, 8, 0], [0, 8, 0]],
        3: [[0, 8, 8], [0, 8, 0], [0, 8, 0]],
        2: [[0, 0, 0], [8, 8, 8], [0, 0, 0]],
    }
    winner = dominant_color(grid)
    return [row[:] for row in prototypes[winner]]
