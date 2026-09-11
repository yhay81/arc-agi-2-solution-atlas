def empty(g, color=0):
    return [[color] * len(g[0]) for _ in g]


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    shifts = {1: (0, 1), 2: (0, -2), 7: (-2, 0), 9: (2, 0)}
    out = empty(g, 8)
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            if v == 8:
                continue
            dr, dc = shifts[v]
            put(out, r + dr, c + dc, v)
    return out
