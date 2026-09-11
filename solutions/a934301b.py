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


def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = cp(g)
    for o in components(g, 0, False, False):
        if sum((g[r][c] == 8 for r, c in o)) >= 2:
            for r, c in o:
                out[r][c] = 0
    return out
