def cp(g):
    return [row[:] for row in g]


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
    objects = components(g, 0, False, False)
    template = next(o for o in objects if len({g[r][c] for r, c in o}) > 1)
    a, b, c, d = bbox(template)
    layers = []
    for color in {g[r][c] for r, c in template}:
        aa, bb, cc, dd = bbox([(r, col) for r, col in template if g[r][col] == color])
        layers.append(((bb - aa + 1) * (dd - cc + 1), color, (aa - a, b - bb, cc - c, d - dd)))
    out = cp(g)
    for obj in objects:
        if obj == template:
            continue
        aa, bb, cc, dd = bbox(obj)
        for area, color, (top, bottom, left, right) in sorted(layers, reverse=True):
            for r in range(aa + top, bb - bottom + 1):
                for col in range(cc + left, dd - right + 1):
                    out[r][col] = color
    return out
