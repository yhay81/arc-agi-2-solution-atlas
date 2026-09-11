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
    h, w = (len(g), len(g[0]))
    side = {c for c in range(w) if all(row[c] != 0 for row in g)}
    refs = {}
    for color in set(sum(g, [])) - {0, 8}:
        pts = [(r, c) for r in range(h) for c in side if g[r][c] == color]
        if pts:
            a, b, c, d = bbox(pts)
            shape = frozenset(((r - a, col - c) for r, col in pts))
            refs[color] = shape

    def canonical(shape):
        variants = []
        for swap in (False, True):
            for sr in (-1, 1):
                for sc in (-1, 1):
                    p = [(sr * (c if swap else r), sc * (r if swap else c)) for r, c in shape]
                    a, b, c, d = bbox(p)
                    variants.append(tuple(sorted(((r - a, col - c) for r, col in p))))
        return min(variants)

    out = cp(g)
    for obj in components(
        [[0 if c in side else v for c, v in enumerate(row)] for row in g], 0, False, False
    ):
        a, b, c, d = bbox(obj)
        if b - a != 4 or d - c != 4:
            raise ValueError("Expected 5x5 tile")
        colors = {g[r][col] for r, col in obj}
        if len(colors) == 1:
            color = next(iter(colors))
            shape = refs[color]
            for r, col in obj:
                out[r][col] = 2
            for r, col in shape:
                out[a + 1 + r][c + 1 + col] = 1
        else:
            shape = {(r - a - 1, col - c - 1) for r, col in obj if g[r][col] == 1}
            matches = [color for color, p in refs.items() if canonical(p) == canonical(shape)]
            if len(matches) != 1:
                raise ValueError("Ambiguous shape code")
            for r, col in obj:
                out[r][col] = matches[0]
    return out
