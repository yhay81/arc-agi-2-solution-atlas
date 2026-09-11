def cp(g):
    return [row[:] for row in g]


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
    a = cp(g)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def opposite(r, c, color):
        return sum(
            (
                0 <= r + dr < h and 0 <= c + dc < w and (a[r + dr][c + dc] == color)
                for dr, dc in dirs
            )
        )

    remove = {(r, c) for r in range(h) for c in range(w) if a[r][c] == 1 and opposite(r, c, 0) >= 3}
    for obj in components(a, 0, False, True):
        if len(obj) <= 2:
            remove.update(obj)
    for r, c in remove:
        a[r][c] = 0
    cleaned = a
    a = cp(g)
    seeds = {
        (r, c)
        for r in range(h)
        for c in range(w)
        if a[r][c] == 0
        and opposite(r, c, 1)
        >= min(3, sum((0 <= r + dr < h and 0 <= c + dc < w for dr, dc in dirs)))
    }
    holes = set(seeds)
    for obj in components([[1 if v == 0 else 0 for v in row] for row in a], 0, False, True):
        if seeds & set(obj) and (not any((r in (0, h - 1) or c in (0, w - 1) for r, c in obj))):
            holes.update(obj)
    out = cp(cleaned)
    for r, c in holes:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                rr, cc = (r + dr, c + dc)
                if 0 <= rr < h and 0 <= cc < w and ((rr, cc) not in holes):
                    out[rr][cc] = 7
    return out
