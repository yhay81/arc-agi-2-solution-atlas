def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


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
    a, b, c, d = bbox(points(g, 1))
    out = [[0] * (d - c + 1) for _ in range(b - a + 1)]
    templates = {}
    masked = [
        [0 if a <= r <= b and c <= col <= d else v for col, v in enumerate(row)]
        for r, row in enumerate(g)
    ]
    for obj in components(masked, 0, True, True):
        top, bottom, left, right = bbox(obj)
        color = g[obj[0][0]][obj[0][1]]
        templates[color] = [(r - top, col - left) for r, col in obj]
    for r in range(a, b + 1):
        for col in range(c, d + 1):
            color = g[r][col]
            if color == 1:
                continue
            for dr, dc in templates[color]:
                put(out, r - a - 1 + dr, col - c - 1 + dc, color)
    return out
