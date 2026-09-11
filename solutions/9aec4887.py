from collections import Counter


def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    fc = [(r, c) for r in range(h) for c in range(w) if a[r][c] not in (0, 8)]
    mc = [(r, c) for r in range(h) for c in range(w) if a[r][c] == 8]
    if not fc or not mc:
        return [r[:] for r in a]
    t, l = min(r for r, c in fc), min(c for r, c in fc)
    b, r = max(r for r, c in fc), max(c for r, c in fc)
    out = [row[l : r + 1] for row in a[t : b + 1]]
    mt, ml = min(x for x, y in mc), min(y for x, y in mc)
    mb, mr = max(x for x, y in mc), max(y for x, y in mc)
    mask = [row[ml : mr + 1] for row in a[mt : mb + 1]]
    if (len(mask), len(mask[0])) != (len(out) - 2, len(out[0]) - 2):
        return [x[:] for x in a]

    def mode(vals):
        q = [v for v in vals if v]
        return Counter(q).most_common(1)[0][0] if q else 0

    sides = (mode(out[0]), mode(out[-1]), mode([x[0] for x in out]), mode([x[-1] for x in out]))
    if 0 in sides or len(set(sides)) != 4:
        return [x[:] for x in a]
    ih, iw = len(mask), len(mask[0])
    interior = [[0] * iw for _ in range(ih)]
    for y in range(ih):
        for x in range(iw):
            if mask[y][x]:
                ds = (y, ih - 1 - y, x, iw - 1 - x)
                m = min(ds)
                ss = [i for i, d in enumerate(ds) if d == m]
                interior[y][x] = sides[ss[0]] if len(ss) == 1 else 8
    for y in range(ih):
        out[y + 1][1:-1] = interior[y]
    return out
