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
    h, w = (len(g), len(g[0]))
    objects = [o for o in components(g, 8, False, False) if any((g[r][c] == 1 for r, c in o))]
    lookup = {p: i for i, o in enumerate(objects) for p in o}
    head = points(g, 4)
    tail = points(g, 2)
    hr, hc = head[0]
    tr, tc = min(tail, key=lambda p: abs(p[0] - hr) + abs(p[1] - hc))
    direction = ((hr > tr) - (hr < tr), (hc > tc) - (hc < tc))
    beam = list(head)
    out = [[8] * w for _ in range(h)]
    for r, c in tail:
        out[r][c] = 2
    seen = set()
    while True:
        beam = [p for p in beam if 0 <= p[0] < h and 0 <= p[1] < w]
        if not beam:
            return out
        hit = next((lookup[p] for p in beam if p in lookup), None)
        for r, c in beam:
            out[r][c] = 2
        if hit is not None:
            if hit in seen:
                return out
            seen.add(hit)
            obj = objects[hit]
            ports = [p for p in obj if g[p[0]][p[1]] == 3]
            a, b, c, d = bbox(obj)
            for r, col in obj:
                out[r][col] = 2
            if all((r == a for r, col in ports)):
                direction = (-1, 0)
            elif all((r == b for r, col in ports)):
                direction = (1, 0)
            elif all((col == c for r, col in ports)):
                direction = (0, -1)
            elif all((col == d for r, col in ports)):
                direction = (0, 1)
            else:
                raise ValueError("Port is not on one side")
            beam = ports
        dr, dc = direction
        beam = [(r + dr, c + dc) for r, c in beam]
