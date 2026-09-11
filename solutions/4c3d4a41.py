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
    grays = components([[5 if v == 5 else 0 for v in row] for row in g], 0, False, True)
    frame = max(grays, key=len)
    key = min(grays, key=len)
    a, b, c, d = bbox(frame)
    ka, kb, kc, kd = bbox(key)
    shift = c + 2 - kc
    out = cp(g)
    for r, col in key:
        out[r][col] = 0
    movedkey = {(r, col + shift) for r, col in key}
    for col in range(c + 1, d):
        ps = [r for r in range(a + 1, b) if g[r][col] not in (0, 5)]
        if not ps:
            continue
        kt = min((r for r, cc in movedkey if cc == col))
        delta = max(0, max(ps) - kt + 1)
        for r in ps:
            out[r][col] = 0
        for r in ps:
            if a < r - delta < b:
                out[r - delta][col] = g[r][col]
    for r, col in movedkey:
        out[r][col] = 5
    return out
