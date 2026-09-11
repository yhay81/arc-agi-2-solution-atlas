from collections import Counter


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
    out = cp(g)
    background = bg(g)
    for obj in components(g, background, True, False):
        reds = [p for p in obj if g[p[0]][p[1]] == 2]
        if not reds:
            raise ValueError("Object has no red mirror")
        a, b, c, d = bbox(reds)
        if len(reds) > 1 and a != b and (c != d):
            raise ValueError("Nonlinear mirror")
        for r, col in obj:
            if g[r][col] == 2:
                continue
            rr, cc = (
                (a + b - r, c + d - col)
                if len(reds) == 1
                else (2 * a - r, col)
                if a == b
                else (r, 2 * c - col)
            )
            put(out, rr, cc, g[r][col])
    return out
