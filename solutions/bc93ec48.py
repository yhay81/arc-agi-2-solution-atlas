from collections import Counter


def cp(g):
    return [row[:] for row in g]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


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
    h, w = (len(g), len(g[0]))
    background = bg(g)
    objects = components(g, background, False, True)
    out = cp(g)
    corners = [(0, 0), (0, w - 1), (h - 1, w - 1), (h - 1, 0)]
    for i, corner in enumerate(corners):
        obj = next((o for o in objects if corner in o), None)
        if obj is None:
            continue
        a, b, c, d = bbox(obj)
        dest = corners[(i + 1) % 4]
        top = 0 if dest[0] == 0 else h - (b - a + 1)
        left = 0 if dest[1] == 0 else w - (d - c + 1)
        for r, col in obj:
            out[top + r - a][left + col - c] = g[r][col]
    return out
