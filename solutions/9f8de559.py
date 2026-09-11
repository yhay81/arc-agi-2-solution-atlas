def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    out = copy(g)
    r, c = next(((r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 2))
    marks = [(x, y) for x, row in enumerate(g) for y, v in enumerate(row) if v == 6]
    nearest = min(marks, key=lambda p: abs(p[0] - r) + abs(p[1] - c))
    dr = (r > nearest[0]) - (r < nearest[0])
    dc = (c > nearest[1]) - (c < nearest[1])
    rr, cc = (r + dr, c + dc)
    while 0 <= rr < len(g) and 0 <= cc < len(g[0]) and (g[rr][cc] == 7):
        rr += dr
        cc += dc
    if 0 <= rr < len(g) and 0 <= cc < len(g[0]):
        out[rr][cc] = 7
    return out
