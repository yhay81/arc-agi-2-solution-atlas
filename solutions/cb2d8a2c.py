def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


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
    start = points(g, 3)[0]
    vertical = start[0] in (0, h - 1)
    if vertical:
        a = [list(row) for row in zip(*g)]
    else:
        a = cp(g)
    hh, ww = (len(a), len(a[0]))
    r, c = points(a, 3)[0]
    direction = 1 if c == 0 else -1
    walls = components([[v if v in (1, 2) else 0 for v in row] for row in a], 0, False, False)
    out = cp(a)
    current = (r, c)

    def line(p, q):
        rr, cc = p
        dr = (q[0] > rr) - (q[0] < rr)
        dc = (q[1] > cc) - (q[1] < cc)
        while (rr, cc) != q:
            out[rr][cc] = 3
            rr += dr
            cc += dc
        out[rr][cc] = 3

    for wall in sorted(walls, key=lambda o: o[0][1], reverse=direction < 0):
        top, bottom, left, right = bbox(wall)
        distance = sum((a[r][c] == 1 for r, c in wall)) + 1
        turn = left - direction * distance
        cross = bottom + distance if top == 0 else top - distance
        if not (0 <= turn < ww and 0 <= cross < hh):
            raise ValueError("Route outside grid")
        q = (current[0], turn)
        line(current, q)
        nxt = (cross, turn)
        line(q, nxt)
        current = nxt
    line(current, (current[0], ww - 1 if direction > 0 else 0))
    for r in range(hh):
        for c in range(ww):
            if a[r][c] in (1, 2):
                out[r][c] = 2
    return [list(row) for row in zip(*out)] if vertical else out
