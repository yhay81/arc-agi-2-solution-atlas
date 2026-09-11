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
    h, w = (len(g), len(g[0]))
    out = cp(g)
    walls = components([[8 if v == 8 else 0 for v in row] for row in g], 0, False, True)
    boxes = [bbox(o) for o in walls]
    fill = next(v for row in g for v in row if v not in (0, 8))
    ports = []
    changed = True
    while changed:
        changed = False
        for i, p in enumerate(boxes):
            for j, q in enumerate(boxes):
                if i >= j:
                    continue
                if max(p[0], q[0]) <= min(p[1], q[1]) and max(p[2], q[2]) <= min(p[3], q[3]):
                    merged = (min(p[0], q[0]), max(p[1], q[1]), min(p[2], q[2]), max(p[3], q[3]))
                    boxes = [x for z, x in enumerate(boxes) if z not in (i, j)] + [merged]
                    changed = True
                    break
            if changed:
                break
    for a, b, c, d in boxes:
        seeds = [(r, col) for r in range(a, b + 1) for col in range(c, d + 1) if g[r][col] == fill]
        seen = set(seeds)
        queue = list(seeds)
        for r, col in queue:
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                rr, cc = (r + dr, col + dc)
                if a <= rr <= b and c <= cc <= d and (g[rr][cc] != 8) and ((rr, cc) not in seen):
                    seen.add((rr, cc))
                    queue.append((rr, cc))
        for r, col in seen:
            out[r][col] = fill
        ports.append(
            [
                (r, col)
                for r, col in seen
                if (r in (a, b) or col in (c, d)) and 0 < r < h - 1 and (0 < col < w - 1)
            ]
        )
    if len(ports) != 2:
        raise ValueError("Two wall systems expected")
    for p in ports[0]:
        for q in ports[1]:
            a, b = (min(p[0], q[0]), max(p[0], q[0]))
            c, d = (min(p[1], q[1]), max(p[1], q[1]))
            for r in range(a, b + 1):
                for col in range(c, d + 1):
                    if g[r][col] != 8:
                        out[r][col] = fill
    return out
