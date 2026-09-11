def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def solve(grid):
    g = grid
    g = cp(g)
    out = cp(g)
    h, w = (len(g), len(g[0]))
    for color in set(v for row in g for v in row) - {0}:
        ps = points(g, color)
        top = [p for p in ps if p[0] == 0]
        if len(top) != 1:
            raise ValueError("Expected one upper endpoint per color")
        r, c = top[0]
        others = [p for p in ps if p != (r, c)]
        if not others:
            for rr in range(h):
                out[rr][c] = color
        elif len(others) == 1:
            a, b = others[0]
            for rr in range(a + 1):
                out[rr][c] = color
            for cc in range(min(b, c), max(b, c) + 1):
                out[a][cc] = color
        else:
            raise ValueError("More than two endpoints")
    return out
