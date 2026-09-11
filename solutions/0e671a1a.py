def solve(grid):
    g = grid
    points = {v: (r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v in (2, 3, 4)}
    out = [r[:] for r in g]
    for start, end in ((2, 4), (4, 3)):
        r, c = points[start]
        a, b = points[end]
        for x in range(min(c, b), max(c, b) + 1):
            if g[r][x] == 0:
                out[r][x] = 5
        for y in range(min(r, a), max(r, a) + 1):
            if g[y][b] == 0:
                out[y][b] = 5
    return out
