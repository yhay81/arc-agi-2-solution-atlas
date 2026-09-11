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
    blue = set(points(g, 1))
    a, b, c, d = bbox(blue)
    mask = [[1 if g[r][col] != 1 else 0 for col in range(c, d + 1)] for r in range(a, b + 1)]
    holes = []
    for o in components(mask, 0, False, True):
        if any((r == 0 or col in (0, d - c) for r, col in o)):
            continue
        holes.append({(r + a, col + c) for r, col in o})
    out = cp(g)
    for obj in components([[v if v == 5 else 0 for v in row] for row in g], 0, False, True):
        shapes = []
        p = list(obj)
        for _ in range(4):
            aa, bb, cc, dd = bbox(p)
            shapes.append({(r - aa, col - cc) for r, col in p})
            p = [(col, -r) for r, col in p]
        fit = False
        for hole in holes:
            hr, hc = min(hole)
            for shape in shapes:
                for sr, sc in shape:
                    moved = {(r + hr - sr, col + hc - sc) for r, col in shape}
                    if (
                        hole <= moved
                        and (not moved & blue)
                        and all(p in hole or p[0] > b for p in moved)
                    ):
                        fit = True
        if fit:
            for r, col in obj:
                out[r][col] = 2
    return out
