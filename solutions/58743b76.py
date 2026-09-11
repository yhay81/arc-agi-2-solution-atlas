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
    g = cp(g)
    h, w = (len(g), len(g[0]))
    black = points(g, 0)
    a, b, c, d = bbox(black)
    out = cp(g)
    palette = []
    for top, left in [(0, 0), (0, w - 2), (h - 2, 0), (h - 2, w - 2)]:
        p = [row[left : left + 2] for row in g[top : top + 2]]
        if all(v not in (0, 8) for row in p for v in row):
            palette.append(p)
    if len(palette) != 1:
        raise ValueError("Expected corner 2x2 palette")
    for r in range(a, b + 1):
        for col in range(c, d + 1):
            if g[r][col] != 0:
                out[r][col] = palette[0][int(r - a >= (b - a + 1) // 2)][
                    int(col - c >= (d - c + 1) // 2)
                ]
    return out
