def cp(g):
    return [row[:] for row in g]


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


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
    objects = components(g, 0, True, False)
    ref = max(objects, key=len)
    marks = [o[0] for o in objects if len(o) == 1]
    horizontal = len({r for r, c in marks}) == 1
    if not (horizontal or len({c for r, c in marks}) == 1):
        raise ValueError("Markers not on one axis")
    marks.sort(key=lambda p: p[1] if horizontal else p[0])
    a, b, c, d = bbox(ref)
    refcolor = g[ref[0][0]][ref[0][1]]
    i0 = next((i for i, p in enumerate(marks) if g[p[0]][p[1]] == refcolor))
    size = d - c + 1 if horizontal else b - a + 1
    anchor = c if horizontal else a
    pos0 = marks[i0][1 if horizontal else 0]
    out = cp(g)
    for i, (r, col) in enumerate(marks):
        shift = (col if horizontal else r) - pos0 + (i - i0) * (size - 1)
        color = g[r][col]
        for rr, cc in ref:
            put(out, rr if horizontal else rr + shift, cc + shift if horizontal else cc, color)
    return out
