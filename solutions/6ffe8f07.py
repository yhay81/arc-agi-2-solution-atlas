def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    a, b, c, d = bbox(points(g, 8))
    out = cp(g)
    for r in range(a, b + 1):
        for start, dc in ((c - 1, -1), (d + 1, 1)):
            col = start
            while 0 <= col < len(g[0]) and g[r][col] != 1:
                out[r][col] = 4
                col += dc
    for col in range(c, d + 1):
        for start, dr in ((a - 1, -1), (b + 1, 1)):
            r = start
            while 0 <= r < len(g) and g[r][col] != 1:
                out[r][col] = 4
                r += dr
    return out
