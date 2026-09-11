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
    cross = next(v for v in g[0] if v != 0)
    frame = next(v for row in g for v in row if v not in (0, cross))
    ps = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == frame]
    top, left, bottom, right = bbox(ps)
    out = [[0 if v == cross else v for v in row] for row in g]
    for r in range(h):
        if out[r][right] == 0:
            out[r][right] = cross
    for c in range(w):
        if out[top][c] == 0:
            out[top][c] = cross
    return out
