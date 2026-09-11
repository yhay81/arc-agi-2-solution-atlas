from collections import Counter


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def empty(g, color=0):
    return [[color] * len(g[0]) for _ in g]


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
    background = bg(g)
    out = empty(g, background)
    for o in components(g, background, False, False):
        colors = {g[r][c] for r, c in o}
        order = sorted(colors, key=lambda v: min((r for r, c in o if g[r][c] == v)))
        if len(order) != 2:
            raise ValueError("Expected upper and lower colors in each object")
        for r, c in o:
            put(out, r, c + (-1 if g[r][c] == order[0] else 1), g[r][c])
    return out
