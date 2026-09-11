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


def shape_key(o):
    shape = normalized_shape(o)
    return min(freeze(transform(shape, t)) for t in range(8))


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


def transform(g, t):
    x = [list(r) for r in g]
    if t >= 4:
        x = [row[::-1] for row in x]
    for _ in range(t % 4):
        x = [list(r) for r in zip(*x[::-1])]
    return x


def normalized_shape(o):
    a, b, c, d = bbox(o)
    return tuple(tuple(int((r, col) in set(o)) for col in range(c, d + 1)) for r in range(a, b + 1))


def freeze(g):
    return tuple(tuple(r) for r in g)


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    a, b, c, d = bbox(points(g, 5))
    objs = components([[0 if v == 5 else v for v in row] for row in g], 0, False, True)
    refs = {}
    out = cp(g)
    for o in objs:
        if all((a <= r <= b and c <= col <= d for r, col in o)):
            key = shape_key(o)
            color = g[o[0][0]][o[0][1]]
            if key in refs and refs[key] != color:
                raise ValueError("Ambiguous shape dictionary")
            refs[key] = color
    for o in objs:
        if g[o[0][0]][o[0][1]] == 3:
            color = refs[shape_key(o)]
            for r, col in o:
                out[r][col] = color
    return out
