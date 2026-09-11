def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    out = copy(g)
    marks = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 8]
    center = next(((r, c) for r, c in marks if 0 < c < len(g[0]) - 1))
    a, b = center
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            rr, cc = (2 * a - r, 2 * b - c)
            if v not in (7, 4, 8) and 0 <= rr < len(g) and (0 <= cc < len(g[0])):
                out[rr][cc] = v
    return out
