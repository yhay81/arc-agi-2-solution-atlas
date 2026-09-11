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
    objects = components(g, 0, True, True)
    templates = {}
    for obj in objects:
        a, b, c, d = bbox(obj)
        color = g[obj[0][0]][obj[0][1]]
        shape = tuple(sorted(((r - a, col - c) for r, col in obj)))
        if color in templates and templates[color] != shape:
            raise ValueError("Inconsistent shape")
        templates[color] = shape
    if len(templates) != 2:
        raise ValueError("Two symbol types expected")
    out = [[0] * len(g[0]) for _ in g]
    for obj in objects:
        a, b, c, d = bbox(obj)
        old = g[obj[0][0]][obj[0][1]]
        new = next(v for v in templates if v != old)
        for dr, dc in templates[new]:
            put(out, a + dr, c + dc, new)
    return out
