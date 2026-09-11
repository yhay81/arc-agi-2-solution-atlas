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
    g = [row[:] for row in g]
    objs = components(g, 0, True, False)
    table = next(
        o
        for o in objs
        if len({g[r][c] for r, c in o}) >= 4
        and len(o) == (bbox(o)[1] - bbox(o)[0] + 1) * (bbox(o)[3] - bbox(o)[2] + 1)
    )
    a, b, c, d = bbox(table)
    p = [row[c : d + 1] for row in g[a : b + 1]]
    colors = {g[r][c] for o in objs if o is not table for r, c in o}
    candidates = []
    if len(p) == 2:
        candidates.extend([dict(zip(p[0], p[1])), dict(zip(p[1], p[0]))])
    if len(p[0]) == 2:
        candidates.extend(
            [
                dict(zip([row[0] for row in p], [row[1] for row in p])),
                dict(zip([row[1] for row in p], [row[0] for row in p])),
            ]
        )
    mapping = max(candidates, key=lambda m: len(set(m) & colors))
    out = cp(g)
    for hole in components([[1 if v == 0 else 0 for v in row] for row in g], 0, False, True):
        if any((r in (0, len(g) - 1) or c in (0, len(g[0]) - 1) for r, c in hole)):
            continue
        border = {
            g[r + dr][c + dc]
            for r, c in hole
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if g[r + dr][c + dc] != 0
        }
        if len(border) == 1 and next(iter(border)) in mapping:
            color = mapping[next(iter(border))]
            for r, c in hole:
                out[r][c] = color
    return out
