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
    g = [row[:] for row in g]
    wall = next(c for c in range(len(g[0])) if all(row[c] == 5 for row in g))
    out = cp(g)
    for o in components(
        [[1 if v == 0 and c < wall else 0 for c, v in enumerate(row)] for row in g], 0, False, True
    ):
        shift = wall - 1 - max((c for r, c in o))
        for r, c in o:
            out[r][c] = 6
        for r, c in o:
            out[r][c + shift] = 0
    mask = [[1 if c < wall and v == 6 else 0 for c, v in enumerate(row)] for row in out]
    for region in components(mask, 0, False, True):
        if any((r in (0, len(g) - 1) or c in (0, wall - 1) for r, c in region)):
            continue
        if max((c for r, c in region)) != wall - 2:
            continue
        for r in {r for r, c in region}:
            for c in range(wall + 1, len(g[0])):
                out[r][c] = 2
    return out
