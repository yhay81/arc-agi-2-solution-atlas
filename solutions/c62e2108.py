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


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = cp(g)
    objects = components([[0 if v == 1 else v for v in row] for row in g], 0, False, True)
    for o in objects:
        a, b, c, d = bbox(o)
        h, w = (b - a + 1, d - c + 1)
        color = g[o[0][0]][o[0][1]]
        if h < 3 or w < 3:
            raise ValueError("Small or nonrectangular seed")
        directions = []
        if any(g[0][col] == 1 for col in range(c, d + 1)):
            directions.append((-h, 0))
        if any(g[-1][col] == 1 for col in range(c, d + 1)):
            directions.append((h, 0))
        if any(g[r][0] == 1 for r in range(a, b + 1)):
            directions.append((0, -w))
        if any(g[r][-1] == 1 for r in range(a, b + 1)):
            directions.append((0, w))
        for dr, dc in directions:
            for n in range(1, max(len(g), len(g[0]))):
                if (
                    a + n * dr >= len(g)
                    or b + n * dr < 0
                    or c + n * dc >= len(g[0])
                    or (d + n * dc < 0)
                ):
                    break
                for r in range(a, b + 1):
                    for col in range(c, d + 1):
                        put(out, r + n * dr, col + n * dc, color if (r, col) in o else 0)
    return out
