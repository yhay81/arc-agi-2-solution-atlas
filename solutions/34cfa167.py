from collections import Counter


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


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    background = bg(g)
    objs = components(g, background, False, True)
    blues = [bbox(o) for o in objs if g[o[0][0]][o[0][1]] == 1]
    (a, b, c, d), (e, f, k, l) = sorted(blues)
    out = cp(g)
    horizontal = g[a][d + 1]
    vertical = g[b + 1][c]
    secondary = g[a][d + 3]
    for top in (a, e):
        for left in (c, k):
            for r in range(top, top + b - a + 1):
                for col in range(left, left + d - c + 1):
                    out[r][col] = 1
    for col in range(d + 1, k):
        color = (
            horizontal
            if (col - d - 1) % 4 == 0
            else secondary
            if (col - d - 1) % 4 == 2
            else background
        )
        for r in list(range(a, b + 1)) + list(range(e, f + 1)):
            out[r][col] = color
        put(out, a - 1, col, horizontal)
        put(out, f + 1, col, horizontal)
    for r in range(b + 1, e):
        color = (
            vertical if (r - b - 1) % 4 == 0 else secondary if (r - b - 1) % 4 == 2 else background
        )
        for col in list(range(c, d + 1)) + list(range(k, l + 1)):
            out[r][col] = color
        put(out, r, c - 1, vertical)
        put(out, r, l + 1, vertical)
    return out
