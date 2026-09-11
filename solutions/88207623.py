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
    objects = components([[v if v in (2, 4) else 0 for v in row] for row in g], 0, True, False)
    for obj in objects:
        reds = [p for p in obj if g[p[0]][p[1]] == 2]
        if not reds:
            continue
        a, b, c, d = bbox(reds)
        if c != d:
            raise ValueError("Expected vertical axis")
        reflected = [(r, 2 * c - col) for r, col in obj if g[r][col] == 4]
        colors = {
            g[r][col]
            for r, col in reflected
            if 0 <= r < len(g) and 0 <= col < len(g[0]) and (g[r][col] not in (0, 2, 4))
        }
        if len(colors) != 1:
            raise ValueError("No unique mirror color")
        for r, col in reflected:
            put(out, r, col, next(iter(colors)))
    return out
