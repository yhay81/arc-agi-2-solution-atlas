def cp(g):
    return [row[:] for row in g]


def transform(g, t):
    x = [list(r) for r in g]
    if t >= 4:
        x = [row[::-1] for row in x]
    for _ in range(t % 4):
        x = [list(r) for r in zip(*x[::-1])]
    return x


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
    choices = [t for t in range(4) if all(row[-1] == 5 for row in transform(g, t))]
    if len(choices) != 1:
        raise ValueError("Expected unique gray boundary")
    t = choices[0]
    x = transform(g, t)
    out = cp(x)
    objects = components(x, 0, False, True)
    objects = [o for o in objects if x[o[0][0]][o[0][1]] != 5]
    objects.sort(key=lambda o: bbox(o)[2])
    for obj in objects:
        a, b, c, d = bbox(obj)
        color = x[obj[0][0]][obj[0][1]]
        for r in range(a, b + 1):
            for col in range(c, len(x[0]) - 1):
                out[r][col] = color
    return transform(out, -t % 4)
