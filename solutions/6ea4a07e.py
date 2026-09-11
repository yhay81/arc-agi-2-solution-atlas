def pal(g):
    return set(v for r in g for v in r)


def solve(grid):
    g = grid
    color = next(iter(pal(g) - {0}))
    new = {5: 4, 8: 2, 3: 1}[color]
    return [[new if v == 0 else 0 for v in row] for row in g]
