def pts(g, color):
    return {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color}


def box(p):
    return (
        min((r for r, c in p)),
        max((r for r, c in p)),
        min((c for r, c in p)),
        max((c for r, c in p)),
    )


def cp(g):
    return [list(r) for r in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    a, b, c, d = box(pts(g, 2))
    o = cp(g)
    for r in range(len(g)):
        for z in range(len(g[0])):
            if r in (a, b) or z in (c, d):
                o[r][z] = 2
            elif a < r < b and c < z < d:
                o[r][z] = 1
    return o
