def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    out = copy(g)
    sep = next((r for r, row in enumerate(g) if all(v == 2 for v in row)))
    top = g[0]
    bottom = g[-1]
    above = sum(v != 0 for v in top) > sum(v != 0 for v in bottom)
    for c, (a, b) in enumerate(zip(top, bottom)):
        if a and b:
            for r in range(1, sep) if above else range(sep + 1, len(g) - 1):
                out[r][c] = 4
    return out
