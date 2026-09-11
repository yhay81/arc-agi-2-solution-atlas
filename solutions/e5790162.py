def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    starts = points(g, 3)
    if len(starts) != 1:
        raise ValueError("Expected one green starting cell")
    r, c = starts[0]
    dr, dc = (0, 1)
    out = cp(g)
    seen = set()
    while 0 <= r < len(g) and 0 <= c < len(g[0]):
        if (r, c, dr, dc) in seen:
            raise ValueError("Loop")
        seen.add((r, c, dr, dc))
        out[r][c] = 3
        a, b = (r + dr, c + dc)
        if 0 <= a < len(g) and 0 <= b < len(g[0]) and (g[a][b] in (6, 8)):
            dr, dc = (-dc, dr) if g[a][b] == 8 else (dc, -dr)
        r += dr
        c += dc
    return out
