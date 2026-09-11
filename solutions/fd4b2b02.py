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
    g = [row[:] for row in g]
    color = next(v for row in g for v in row if v)
    a, b, c, d = bbox(points(g, color))
    out = cp(g)
    h, w = (len(g), len(g[0]))
    for dr in (-1, 1):
        for dc in (-1, 1):
            aa, bb, cc, dd = (a, b, c, d)
            v = color
            for _ in range(h + w):
                nh, nw = (dd - cc + 1, bb - aa + 1)
                rr = aa - nh if dr < 0 else bb + 1
                col = cc - nw if dc < 0 else dd + 1
                aa, bb, cc, dd = (rr, rr + nh - 1, col, col + nw - 1)
                v = 6 if v == 3 else 3
                if bb < 0 or aa >= h or dd < 0 or (cc >= w):
                    break
                for r in range(aa, bb + 1):
                    for c0 in range(cc, dd + 1):
                        put(out, r, c0, v)
    return out
