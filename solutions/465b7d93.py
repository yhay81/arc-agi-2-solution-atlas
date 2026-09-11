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


def crop(g, cells):
    a, b, c, d = bbox(cells)
    return [list(row[c : d + 1]) for row in g[a : b + 1]]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    a, b, c, d = bbox(points(g, 6))
    ps = [(r, col) for r, row in enumerate(g) for col, v in enumerate(row) if v not in (6, 7)]
    patch = crop(g, ps)
    out = cp(g)
    for r, col in ps:
        out[r][col] = 7
    ph, pw = (len(patch), len(patch[0]))
    height, width = (b - a - 1, d - c - 1)
    if len(set(v for row in patch for v in row)) == 1:
        for r in range(a + 1, b):
            for col in range(c + 1, d):
                out[r][col] = patch[0][0]
        return out

    def coord(r, col):
        return (
            a + 1 + round(r * (height - 1) / max(1, ph - 1)),
            c + 1 + round(col * (width - 1) / max(1, pw - 1)),
        )

    for r, row in enumerate(patch):
        for col, v in enumerate(row):
            if v == 7:
                continue
            rr, cc = coord(r, col)
            out[rr][cc] = v
            for nr, nc in [(r + 1, col), (r, col + 1)]:
                if nr < ph and nc < pw and (patch[nr][nc] == v):
                    er, ec = coord(nr, nc)
                    for ar in range(rr, er + 1):
                        for ac in range(cc, ec + 1):
                            out[ar][ac] = v
    return out
