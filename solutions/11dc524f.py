from collections import Counter


def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    bg = Counter(v for row in a for v in row).most_common(1)[0][0]
    colors = {v for row in a for v in row if v != bg}

    def points(color):
        return [(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == color]

    def bounds(ps):
        rs, cs = [p[0] for p in ps], [p[1] for p in ps]
        return min(rs), min(cs), max(rs), max(cs)

    block = next(
        c
        for c in colors
        if len(points(c)) == 4
        and bounds(points(c))[2] - bounds(points(c))[0] == 1
        and bounds(points(c))[3] - bounds(points(c))[1] == 1
    )
    color = next(c for c in colors if c != block)
    p, q = points(color), points(block)
    y, x, v, u = bounds(p)
    by, bx, bv, bu = bounds(q)
    if u < bx:
        delta = (0, bx - u - 1)
        axis = 1
        mirror = 2 * bx - 1
    elif x > bu:
        delta = (0, bu - x + 1)
        axis = 1
        mirror = 2 * bu + 1
    elif v < by:
        delta = (by - v - 1, 0)
        axis = 0
        mirror = 2 * by - 1
    else:
        delta = (bv - y + 1, 0)
        axis = 0
        mirror = 2 * bv + 1
    moved = [(r + delta[0], c + delta[1]) for r, c in p]
    ref = [(mirror - r if axis == 0 else r, mirror - c if axis == 1 else c) for r, c in moved]
    o = [[bg] * w for _ in range(h)]
    for r, c in moved:
        o[r][c] = color
    for r, c in ref:
        o[r][c] = block
    return o
