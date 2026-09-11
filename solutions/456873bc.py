def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


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
    objects = components([[2 if v == 2 else 0 for v in row] for row in g], 0, True, True)
    obj = max(objects, key=len)
    a, b, c, d = bbox(obj)
    ph, pw = (b - a + 1, d - c + 1)
    shape = {(r - a, col - c) for r in range(a, b + 1) for col in range(c, d + 1) if g[r][col] == 2}
    out = [[0] * len(g[0]) for _ in g]
    for br, bc in shape:
        for dr, dc in shape:
            put(out, br * (ph + 1) + dr, bc * (pw + 1) + dc, 8 if (dr, dc) == (br, bc) else 2)
    return out
