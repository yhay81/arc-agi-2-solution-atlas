def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def transform(g, t):
    x = [list(r) for r in g]
    if t >= 4:
        x = [row[::-1] for row in x]
    for _ in range(t % 4):
        x = [list(r) for r in zip(*x[::-1])]
    return x


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
    shape = crop(g, [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != 0])
    h, w = (len(shape), len(shape[0]))
    out = [[0] * (2 * w + h) for _ in range(2 * w + h)]
    for block, top, left in [
        (shape, w, 0),
        (transform(shape, 4), w, w + h),
        (transform(shape, 1), 0, w),
        (transform(transform(shape, 1), 6), w + h, w),
    ]:
        for r, row in enumerate(block):
            for c, v in enumerate(row):
                put(out, top + r, left + c, v)
    return out
