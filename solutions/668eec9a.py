def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def solve(grid):
    g = grid
    cs = set(v for row in g for v in row) - {7}
    order = sorted(cs, key=lambda c: min((r for r, col in points(g, c))))
    if len(order) > 5:
        raise ValueError("Too many colors")
    return [[7] * 3 for _ in range(5 - len(order))] + [[c] * 3 for c in order]
