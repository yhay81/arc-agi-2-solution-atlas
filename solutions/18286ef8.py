def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    a, b, c, d = bbox(points(g, 5))
    out = cp(g)
    cr, cc = ((a + b) // 2, (c + d) // 2)
    if b - a != 2 or d - c != 2:
        raise ValueError("Expected gray 3x3")
    marker = points(g, 6)
    if len(marker) != 1:
        raise ValueError("Expected one purple instruction")
    r, col = marker[0]
    dr = (r > b) - (r < a)
    dc = (col > d) - (col < c)
    out[cr][cc] = 5
    out[cr + dr][cc + dc] = 9
    out[r][col] = 9
    return out
