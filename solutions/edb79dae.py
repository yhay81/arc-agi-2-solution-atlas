from collections import Counter


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


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
    g = [row[:] for row in g]
    base = bg(g)
    frame = points(g, 5)
    a, b, c, d = bbox(frame)
    out = [row[c : d + 1] for row in g[a : b + 1]]
    outside = [
        [base if a <= r <= b and c <= col <= d else v for col, v in enumerate(row)]
        for r, row in enumerate(g)
    ]
    objs = components(outside, base, True, False)
    mapping = {}
    templates = {}
    for obj in objs:
        aa, bb, cc, dd = bbox(obj)
        colors = {g[r][col] for r, col in obj}
        if len(colors) == 2 and len(obj) == (bb - aa + 1) * (dd - cc + 1):
            src = g[aa][cc]
            mapping[src] = next(v for v in colors if v != src)
        elif len(colors) == 1:
            color = next(iter(colors))
            obj = obj + (templates[color][4] if color in templates else [])
            aa, bb, cc, dd = bbox(obj)
            templates[color] = (aa, bb, cc, dd, obj)
    for obj in components([[base if v == 5 else v for v in row] for row in out], base, False, True):
        color = out[obj[0][0]][obj[0][1]]
        aa, bb, cc, dd = bbox(obj)
        ta, tb, tc, td, shape = templates[color]
        if (bb - aa, dd - cc) != (tb - ta, td - tc):
            raise ValueError("Shape and tile dimensions differ")
        for r, col in obj:
            out[r][col] = base
        for r, col in shape:
            out[aa + r - ta][cc + col - tc] = mapping[color]
    return out
