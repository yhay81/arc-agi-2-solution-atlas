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
    g = [list(row) for row in g]
    p = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v}
    a, b, c, d = box(p)
    r = (a + b) // 2
    z = (c + d) // 2
    o = cp(g)
    o[r][z] = 5
    for rr, cc_ in p:
        o[r + (1 if rr > r else -1)][z + (1 if cc_ > z else -1)] = g[rr][cc_]
    return o
