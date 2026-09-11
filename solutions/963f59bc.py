def cp(g):
    return [row[:] for row in g]


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


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
    source = points(g, 1)
    a, b, c, d = bbox(source)
    out = cp(g)
    for r, row in enumerate(g):
        for col, color in enumerate(row):
            if color in (0, 1):
                continue
            if a <= r <= b:
                anchors = [p for p in source if p[0] == r]
                if len(anchors) != 1:
                    raise ValueError("Horizontal anchor not unique")
                axis = col + anchors[0][1]
                for rr, cc in source:
                    put(out, rr, axis - cc, color)
            else:
                anchors = [p for p in source if p[1] == col]
                if len(anchors) != 1:
                    raise ValueError("Vertical anchor not unique")
                axis = r + anchors[0][0]
                for rr, cc in source:
                    put(out, axis - rr, cc, color)
    return out
