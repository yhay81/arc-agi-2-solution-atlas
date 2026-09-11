def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


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
    background = 7
    green = points(g, 3)
    a, b, c, d = bbox(green)
    legend = {g[r][col] for r in range(a, b + 1) for col in range(c, d + 1)} - {background, 3}
    out = cp(g)
    for obj in components(g, background, False, False):
        top, bottom, left, right = bbox(obj)
        colors = {g[r][col] for r, col in obj}
        if legend <= colors:
            for r in range(top, bottom + 1):
                for col in range(left, right + 1):
                    out[r][col] = background
    return out
