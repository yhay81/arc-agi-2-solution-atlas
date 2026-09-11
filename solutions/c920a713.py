from collections import Counter
from itertools import permutations


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    colors = sorted({v for row in g for v in row if v != 0})
    above = {c: Counter() for c in colors}
    for color in colors:
        cells = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]
        top = min((r for r, c in cells))
        bottom = max((r for r, c in cells))
        left = min((c for r, c in cells))
        right = max((c for r, c in cells))
        border = {
            (r, c)
            for r in range(top, bottom + 1)
            for c in range(left, right + 1)
            if r in (top, bottom) or c in (left, right)
        }
        for r, c in border:
            if g[r][c] not in (0, color):
                above[color][g[r][c]] += 1
    best = -1
    orders = []
    for candidate in permutations(colors):
        ranks = {color: i for i, color in enumerate(candidate)}
        score = sum(
            (
                weight
                for color, front in above.items()
                for other, weight in front.items()
                if ranks[color] < ranks[other]
            )
        )
        if score > best:
            best = score
            orders = [candidate]
        elif score == best:
            orders.append(candidate)
    if len(orders) != 1:
        raise ValueError("Most consistent occlusion order is not unique")
    order = orders[0]
    n = 2 * len(order) - 1
    return [[order[min(r, c, n - 1 - r, n - 1 - c)] for c in range(n)] for r in range(n)]
