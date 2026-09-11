import math


def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    out = copy(g)
    center = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 4]
    cr = sum((r for r, c in center)) / len(center)
    cc = sum((c for r, c in center)) / len(center)
    colors = {v for row in g for v in row if v not in (4, 7)}
    objects = []
    for color in colors:
        ps = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]
        angle = math.atan2(
            sum((r for r, c in ps)) / len(ps) - cr, sum((c for r, c in ps)) / len(ps) - cc
        )
        objects.append((angle, color, ps))
    objects.sort()
    for i, (_, color, ps) in enumerate(objects):
        replacement = objects[i - 1][1]
        for r, c in ps:
            out[r][c] = replacement
    return out
