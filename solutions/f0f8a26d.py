def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def empty(g, color=0):
    return [[color] * len(g[0]) for _ in g]


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
    objects = components(g, 7, False, True)
    out = empty(g, 7)
    for o in objects:
        a, b, c, d = bbox(o)
        cr, cc = ((a + b) // 2, (c + d) // 2)
        color = g[o[0][0]][o[0][1]]
        if (a != b and c != d) or len(o) % 2 == 0:
            raise ValueError("Expected odd straight rod")
        for r, col in o:
            put(out, cr - (col - cc), cc + (r - cr), color)
    return out
