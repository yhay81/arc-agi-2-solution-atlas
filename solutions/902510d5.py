from collections import Counter


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
    h, w = (len(g), len(g[0]))
    objects = components(g, 0, True, True)
    arrow = max(objects, key=len)
    corners = [
        (r, c)
        for r, c in ((0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1))
        if g[r][c] != 0 and (r, c) not in arrow
    ]
    if len(corners) != 1:
        raise ValueError("One corner marker expected")
    corner = corners[0]
    markers = [(r, c) for obj in objects if obj is not arrow for r, c in obj if (r, c) != corner]
    counts = Counter((g[r][c] for r, c in markers))
    fill = counts.most_common(1)[0][0]
    out = [[0] * w for _ in g]
    for r, c in arrow:
        out[r][c] = g[r][c]
    for r in range(h):
        for c in range(w):
            if abs(r - corner[0]) + abs(c - corner[1]) < len(markers):
                out[r][c] = fill
    return out
