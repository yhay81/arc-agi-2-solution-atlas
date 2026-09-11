from collections import Counter


def cp(g):
    return [row[:] for row in g]


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


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
    base = bg(g)
    wall = Counter(v for row in g for v in row if v != base).most_common(1)[0][0]
    out = cp(g)
    h, w = (len(g), len(g[0]))
    main = set(max(components(g, base, True, False), key=len))
    regions = sorted(
        components([[1 if v == base else 0 for v in row] for row in g], 0, False, True),
        key=len,
        reverse=True,
    )
    for obj in regions[2:]:
        edges = {
            e
            for r, c in obj
            for e, yes in [
                ("top", r == 0),
                ("bottom", r == h - 1),
                ("left", c == 0),
                ("right", c == w - 1),
            ]
            if yes
        }
        boundary = {
            (r + dr, c + dc)
            for r, c in obj
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if 0 <= r + dr < h and 0 <= c + dc < w and (g[r + dr][c + dc] != base)
        }
        if boundary <= main:
            for r, c in obj:
                out[r][c] = wall
    return out
