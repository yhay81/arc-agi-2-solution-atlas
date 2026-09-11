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
    background = bg(g)
    objs = components(g, background, False, True)
    small = [o[0] for o in objs if len(o) == 1]
    big = [o for o in objs if len(o) > 1]
    r0 = min((r for r, c in small))
    c0 = min((c for r, c in small))
    template = [((r - r0) // 2, (c - c0) // 2, g[r][c]) for r, c in small]
    anchors = []
    for o in big:
        a, b, c, d = bbox(o)
        anchors.append((a, c, g[a][c], b - a + 1, d - c + 1))
    sizes = {(x[3], x[4]) for x in anchors}
    if len(sizes) != 1:
        raise ValueError("Unequal anchor sizes")
    sh, sw = next(iter(sizes))
    candidates = []
    for step in range(max(sh, sw), 31):
        ar, ac, color, _, _ = anchors[0]
        for r, c, v in template:
            if v != color:
                continue
            top, left = (ar - r * step, ac - c * step)
            expanded = {(top + rr * step, left + cc * step, vv) for rr, cc, vv in template}
            if all(((rr, cc, vv) in expanded for rr, cc, vv, _, _ in anchors)):
                candidates.append((step, top, left))
    candidates = list(set(candidates))
    if len(candidates) != 1:
        raise ValueError("Scale ambiguous")
    step, top, left = candidates[0]
    out = cp(g)
    for r, c, v in template:
        for dr in range(sh):
            for dc in range(sw):
                put(out, top + r * step + dr, left + c * step + dc, v)
    return out
