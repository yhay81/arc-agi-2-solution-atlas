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
    h = len(g)
    w = (len(g[0]) - 2) // 3
    out = [[7] * w for _ in range(h)]
    for i in range(3):
        panel = [row[i * (w + 1) : i * (w + 1) + w] for row in g]
        objects = components(panel, 7, False, True)
        objects.sort(key=lambda o: sum((c for r, c in o)) / len(o))
        if len(objects) != 3:
            raise ValueError("Three side-by-side objects expected")
        for r, c in objects[i]:
            out[r][c] = panel[r][c]
    return out
