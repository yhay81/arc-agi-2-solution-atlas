from collections import Counter


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    "Order overlapping full-grid lines from most hidden to most visible."
    h, w = len(a), len(a[0])
    hidden = {}
    for color in sorted({v for row in a for v in row} - {7}):
        positions = [(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == color]
        counts = [
            Counter((r for r, c in positions)),
            Counter((c for r, c in positions)),
            Counter((r - c for r, c in positions)),
            Counter((r + c for r, c in positions)),
        ]
        maxima = [max(x.values()) for x in counts]
        family = maxima.index(max(maxima))
        if family == 0:
            expected = w
        elif family == 1:
            expected = h
        elif family == 2:
            diagonal = max(counts[2], key=counts[2].get)
            expected = min(h - 1, w - 1 + diagonal) - max(0, diagonal) + 1
        else:
            diagonal = max(counts[3], key=counts[3].get)
            expected = min(h - 1, diagonal) - max(0, diagonal - w + 1) + 1
        hidden[color] = expected - len(positions)
    return [sorted(hidden, key=lambda color: (-hidden[color], -color))]
