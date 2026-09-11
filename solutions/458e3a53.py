def bbox(ps):
    return (
        min((r for r, c in ps)),
        min((c for r, c in ps)),
        max((r for r, c in ps)),
        max((c for r, c in ps)),
    )


def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    rows = [r for r, row in enumerate(g) if len(set(row)) == 1]
    cols = [c for c in range(w) if len({row[c] for row in g}) == 1]
    rb = [-1] + rows + [h]
    cb = [-1] + cols + [w]
    hits = []
    for i, (a, b) in enumerate(zip(rb, rb[1:])):
        for j, (c, d) in enumerate(zip(cb, cb[1:])):
            values = {g[r][k] for r in range(a + 1, b) for k in range(c + 1, d)}
            if len(values) == 1:
                hits.append((i, j, next(iter(values))))
    top, left, bottom, right = bbox([(r, c) for r, c, v in hits])
    out = [[0] * (right - left + 1) for _ in range(bottom - top + 1)]
    for r, c, v in hits:
        out[r - top][c - left] = v
    return out
