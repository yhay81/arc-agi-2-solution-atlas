from collections import Counter


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
    h, w = (len(g), len(g[0]))
    base = 8
    corner = next(
        ((r, c) for r, c in [(0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1)] if g[r][c] == 0)
    )
    vertical = Counter(g[corner[0]]).most_common(1)[0][0] == 2
    clean = cp(g)
    for c in range(w):
        clean[corner[0]][c] = base
    for r in range(h):
        clean[r][corner[1]] = base
    objects = components(clean, base, True, False)

    def key(o):
        a, b, c, d = bbox(o)
        rr = a if corner[0] == 0 else h - 1 - b
        cc = c if corner[1] == 0 else w - 1 - d
        return (cc, rr) if vertical else (rr, cc)

    pieces = []
    for o in sorted(objects, key=key):
        a, b, c, d = bbox(o)
        p = [row[c : d + 1] for row in clean[a : b + 1]]
        if vertical:
            p = [list(row) for row in zip(*p)][::-1]
        pieces.append(p)
    width = max(len(p[0]) for p in pieces)
    out = []
    for p in pieces:
        left = (width - len(p[0])) // 2
        out.extend([[base] * left + row + [base] * (width - left - len(row)) for row in p])
    return out
