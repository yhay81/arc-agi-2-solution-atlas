def cp(g):
    return [row[:] for row in g]


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
    g = cp(g)
    objects = components([[8 if v in (8, 9) else 7 for v in row] for row in g], 7, False, True)
    source = next(o for o in objects if any((g[r][c] == 9 for r, c in o)))
    target = min((o for o in objects if len(o) > len(source)), key=len)
    a, b, c, d = bbox(source)
    top = g[a][c] == 9
    out = cp(g)
    for r, col in source:
        out[r][col] = 8
    a, b, c, d = bbox(target)
    half = len(target) // 2
    for r in range(a, a + half) if top else range(b - half + 1, b + 1):
        out[r][c] = 9
    return out
