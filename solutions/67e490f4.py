from collections import Counter


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


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


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


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
    background = bg(g)
    non = components(g, background, False, False)
    target = max(non, key=len)
    wall = Counter((g[r][col] for r, col in target)).most_common(1)[0][0]
    a, b, c, d = bbox(points(g, wall))
    out = [row[c : d + 1] for row in g[a : b + 1]]

    def signature(obj):
        aa, bb, cc, dd = bbox(obj)
        s = [[int((r, col) in set(obj)) for col in range(cc, dd + 1)] for r in range(aa, bb + 1)]
        return min(tuple(map(tuple, transform(s, t))) for t in range(8))

    votes = {}
    rest = [
        [background if a <= r <= b and c <= col <= d else v for col, v in enumerate(row)]
        for r, row in enumerate(g)
    ]
    for obj in components(rest, background, False, True):
        votes.setdefault(signature(obj), Counter())[g[obj[0][0]][obj[0][1]]] += 1
    for hole in components(
        [[1 if v == background else 0 for v in row] for row in out], 0, False, True
    ):
        counts = votes.get(signature(hole))
        if not counts:
            raise ValueError("No same-shape exemplar")
        color = counts.most_common(1)[0][0]
        for r, col in hole:
            out[r][col] = color
    return out
