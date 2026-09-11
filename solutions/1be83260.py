from collections import Counter


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


def crop(g, cells):
    a, b, c, d = bbox(cells)
    return [list(row[c : d + 1]) for row in g[a : b + 1]]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    objs = components(g, 0, False, False)
    shapes = [crop(g, o) for o in objs]
    ref = [p for p in shapes if len(set(v for row in p for v in row) - {0}) > 1]
    if len(ref) != 1:
        raise ValueError("Expected one multicolor reference tile")
    ref = ref[0]
    base = Counter(v for row in ref for v in row if v != 0).most_common(1)[0][0]
    rs = sorted({r for r, row in enumerate(ref) for c, v in enumerate(row) if v != base})
    cs = sorted({c for r, row in enumerate(ref) for c, v in enumerate(row) if v != base})
    palette = [[ref[r][c] or base for c in cs] for r in rs]
    allcells = sum(objs, [])
    a, b, c, d = bbox(allcells)
    out = [[base] * (d - c + 1) for _ in range(b - a + 1)]
    tops = sorted({bbox(o)[0] for o in objs})
    lefts = sorted({bbox(o)[2] for o in objs})
    if len(tops) != len(palette) or len(lefts) != len(palette[0]):
        raise ValueError("Palette/tile count mismatch")
    for o in objs:
        rr, bb, cc, dd = bbox(o)
        color = palette[tops.index(rr)][lefts.index(cc)]
        for r in range(rr, bb + 1):
            for col in range(cc, dd + 1):
                out[r - a][col - c] = color if g[r][col] == base else base
    return out
