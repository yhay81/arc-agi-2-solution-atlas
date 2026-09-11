def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    rows = [r for r in range(h) if len(set(a[r])) == 1 and a[r][0]]
    cols = [c for c in range(w) if len({a[r][c] for r in range(h)}) == 1 and a[0][c]]
    if len(rows) != 1 or len(cols) != 1:
        return [r[:] for r in a]
    r, c = rows[0], cols[0]
    qs = [
        [row[:c] for row in a[:r]],
        [row[c + 1 :] for row in a[:r]],
        [row[:c] for row in a[r + 1 :]],
        [row[c + 1 :] for row in a[r + 1 :]],
    ]
    keys = [(i, q) for i, q in enumerate(qs) if q and q[0] and all(v for row in q for v in row)]
    masks = [
        (i, q)
        for i, q in enumerate(qs)
        if q and q[0] and any(v for row in q for v in row) and any(not v for row in q for v in row)
    ]
    if len(keys) != 1 or len(masks) != 1 or keys[0][0] + masks[0][0] != 3:
        return [x[:] for x in a]
    key, mask = keys[0][1], masks[0][1]
    mh, mw = len(mask), len(mask[0])
    kh, kw = len(key), len(key[0])
    if mh % kh or mw % kw:
        return [x[:] for x in a]
    sy, sx = mh // kh, mw // kw
    colored = [[key[y // sy][x // sx] if mask[y][x] else 0 for x in range(mw)] for y in range(mh)]
    return colored
