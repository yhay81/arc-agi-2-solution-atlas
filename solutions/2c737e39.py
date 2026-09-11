def cp(g):
    return [row[:] for row in g]


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


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
    objects = components(g, 0, False, False)
    ref = [o for o in objects if len(o) > 1 and any((g[r][c] == 5 for r, c in o))]
    if len(ref) != 1:
        raise ValueError("Expected one anchored template")
    reference = ref[0]
    anchors = [p for p in reference if g[p[0]][p[1]] == 5]
    if len(anchors) != 1:
        raise ValueError("Expected one template anchor")
    a, b = anchors[0]
    out = cp(g)
    for r, c in points(g, 5):
        if (r, c) == (a, b):
            continue
        out[r][c] = 0
        for rr, cc in reference:
            if g[rr][cc] != 5:
                put(out, r + rr - a, c + cc - b, g[rr][cc])
    return out
