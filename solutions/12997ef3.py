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
    template = crop(g, points(g, 1))
    marks = [(r, c, v) for r, row in enumerate(g) for c, v in enumerate(row) if v not in (0, 1)]
    if len(template) != 3 or len(template[0]) != 3:
        raise ValueError("Expected 3x3 shape")
    horizontal = len({r for r, c, v in marks}) == 1
    marks.sort(key=lambda p: p[1] if horizontal else p[0])
    blocks = [[[v if a == 1 else 0 for a in row] for row in template] for r, c, v in marks]
    return (
        [sum((block[r] for block in blocks), []) for r in range(3)]
        if horizontal
        else sum(blocks, [])
    )
