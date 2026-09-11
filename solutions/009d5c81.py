def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


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
    marker = crop(g, points(g, 1))
    styles = {
        (0, 1, 0, 1, 1, 1, 0, 1, 0): 2,
        (1, 1, 1, 1, 0, 1, 0, 1, 0): 7,
        (1, 0, 1, 0, 1, 0, 1, 1, 1): 3,
    }
    key = tuple(int(v == 1) for row in marker for v in row)
    if key not in styles:
        raise ValueError("Unknown marker shape")
    return [[styles[key] if v == 8 else 0 if v == 1 else v for v in row] for row in g]
