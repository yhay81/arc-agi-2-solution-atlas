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
    a, b, c, d = bbox(points(g, 0))
    out = cp(g)
    for r in range(len(g)):
        for col in range(len(g[0])):
            if (a <= r <= b or c <= col <= d) and g[r][col] != 2:
                out[r][col] = 0
    return out
