def crop(g, cells):
    a, b, c, d = bbox(cells)
    return [list(row[c : d + 1]) for row in g[a : b + 1]]


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
    h, w = (len(g), len(g[0]))
    rs = [r for r, row in enumerate(g) if len(set(row)) == 1 and row[0] != 0]
    cs = [c for c in range(w) if len({row[c] for row in g}) == 1 and g[0][c] != 0]
    if len(rs) != 1 or len(cs) != 1:
        raise ValueError("Expected one separator cross")
    out = [[0] * 6 for _ in range(6)]
    for ir, (a, b) in enumerate(zip([-1] + rs, rs + [h])):
        for ic, (c, d) in enumerate(zip([-1] + cs, cs + [w])):
            panel = [row[c + 1 : d] for row in g[a + 1 : b]]
            cells = [(r, col) for r, row in enumerate(panel) for col, v in enumerate(row) if v != 0]
            obj = crop(panel, cells)
            if len(obj) > 3 or len(obj[0]) > 3:
                raise ValueError("Oversized object")
            for r, row in enumerate(obj):
                for col, v in enumerate(row):
                    out[ir * 3 + r][ic * 3 + col] = v
    return out
