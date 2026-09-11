from collections import Counter


def transform(g, t):
    x = [list(r) for r in g]
    if t >= 4:
        x = [row[::-1] for row in x]
    for _ in range(t % 4):
        x = [list(r) for r in zip(*x[::-1])]
    return x


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
    objects = components(g, 0, False, False)
    ref = max(objects, key=len)
    markers = [o[0] for o in objects if len(o) == 1]
    shape = crop(g, ref)
    rare = Counter((g[r][c] for r, c in ref))
    colors = {g[r][c] for r, c in markers}
    matches = []
    for t in range(8):
        p = transform(shape, t)
        inside = {v: (r, c) for r, row in enumerate(p) for c, v in enumerate(row) if v in colors}
        deltas = {(r - inside[g[r][c]][0], c - inside[g[r][c]][1]) for r, c in markers}
        if len(deltas) == 1:
            matches.append(p)
    if len(matches) != 1:
        raise ValueError("Ambiguous orientation")
    return matches[0]
