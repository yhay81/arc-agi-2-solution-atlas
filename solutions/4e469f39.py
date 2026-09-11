def cp(g):
    return [row[:] for row in g]


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
    out = cp(g)
    for obj in components(g, 0, False, True):
        a, b, c, d = bbox(obj)
        holes = [col for col in range(c, d + 1) if g[a][col] == 0]
        if len(holes) != 1:
            raise ValueError("One top opening expected")
        opening = holes[0]
        for r in range(a, b + 1):
            for col in range(c, d + 1):
                if g[r][col] == 0:
                    out[r][col] = 2
        for col in range(opening, len(g[0])) if opening < (c + d) / 2 else range(opening + 1):
            put(out, a - 1, col, 2)
    return out
