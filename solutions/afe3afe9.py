def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def components(g, background=0, diagonal=False, mono=True):
    unseen = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != background}
    out = []
    while unseen:
        p = min(unseen)
        unseen.remove(p)
        q = [p]
        cells = []
        for r, c in q:
            cells.append((r, c))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if not (dr or dc) or (not diagonal and dr and dc):
                        continue
                    n = (r + dr, c + dc)
                    if n in unseen and (not mono or g[n[0]][n[1]] == g[r][c]):
                        unseen.remove(n)
                        q.append(n)
        out.append(cells)
    return out


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    rings = []
    for obj in components(g, 0, False, True):
        a, b, c, d = bbox(obj)
        if b - a == 2 and d - c == 2 and (len(obj) == 8):
            rings.append((a + 1, c + 1, g[a][c]))
    rows = sorted({r for r, c, v in rings})
    cols = sorted({c for r, c, v in rings})
    out = [[0] * len(cols) for _ in rows]
    for r, c, v in rings:
        out[rows.index(r)][cols.index(c)] = v
    side = (
        "top"
        if all(v == 1 for v in g[0])
        else "bottom"
        if all(v == 1 for v in g[-1])
        else "left"
        if all(row[0] == 1 for row in g)
        else "right"
    )
    if side in ("top", "bottom"):
        for r, row in enumerate(out):
            values = [v for v in row if v]
            out[r] = (
                [0] * (len(row) - len(values)) + values
                if side == "top"
                else values + [0] * (len(row) - len(values))
            )
    else:
        for c in range(len(cols)):
            values = [row[c] for row in out if row[c]]
            values = (
                values + [0] * (len(rows) - len(values))
                if side == "left"
                else [0] * (len(rows) - len(values)) + values
            )
            for r, v in enumerate(values):
                out[r][c] = v
    return out
