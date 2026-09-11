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
    h, w = (len(g), len(g[0]))
    objects = components(g, 0, True, False)
    mapping = {}
    targets = []
    for obj in objects:
        a, b, c, d = bbox(obj)
        colors = {g[r][col] for r, col in obj}
        if (
            len(colors) > 1
            and b - a == 1
            and (d - c == 1)
            and all(g[a][col] == g[b][col] for col in (c, d))
        ):
            mapping[g[a][c]] = g[a][d]
        else:
            targets.append(obj)
    out = cp(g)
    for obj in targets:
        color = g[obj[0][0]][obj[0][1]]
        if color not in mapping:
            raise ValueError("No legend color")
        shape = set(obj)
        a, b, c, d = bbox(obj)
        a -= 1
        b += 1
        c -= 1
        d += 1
        outside = {(a, c)}
        queue = [(a, c)]
        for r, col in queue:
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                p = (r + dr, col + dc)
                if a <= p[0] <= b and c <= p[1] <= d and (p not in shape) and (p not in outside):
                    outside.add(p)
                    queue.append(p)
        for r, col in outside:
            put(out, r, col, mapping[color])
    return out
