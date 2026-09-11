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
    h, w = (len(g), len(g[0]))
    rects = []
    for color in set(v for row in g for v in row):
        for obj in components(
            [[v if v == color else -1 for v in row] for row in g], -1, False, True
        ):
            a, b, c, d = bbox(obj)
            if b > a and d > c and (len(obj) == (b - a + 1) * (d - c + 1)):
                rects.append(obj)
    hidden = set(p for obj in rects for p in obj)
    a, b, c, d = bbox(max(rects, key=len))
    candidates = []
    for ph in range(1, 9):
        for pw in range(1, 9):
            cells = {}
            for r, row in enumerate(g):
                for col, v in enumerate(row):
                    if (r, col) not in hidden:
                        cells.setdefault((r % ph, col % pw), set()).add(v)
            if len(cells) == ph * pw and all(len(s) == 1 for s in cells.values()):
                candidates.append((ph * pw, ph, pw, {p: next(iter(s)) for p, s in cells.items()}))
    if not candidates:
        raise ValueError("No periodic background")
    _, ph, pw, tile = min(candidates, key=lambda t: t[:3])
    return [[tile[r % ph, col % pw] for col in range(c, d + 1)] for r in range(a, b + 1)]
