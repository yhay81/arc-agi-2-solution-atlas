from collections import Counter


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


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    base = bg(g)
    gates = components([[v if v == 4 else base for v in row] for row in g], base, False, True)
    upper = min(gates, key=lambda o: min((r for r, c in o)))
    lower = max(gates, key=lambda o: max((r for r, c in o)))
    shift = bbox(upper)[2] - bbox(lower)[2]
    obj = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v not in (base, 4)]
    drop = len(g) - 1 - max((r for r, c in obj))
    out = cp(g)
    for r, c in obj:
        out[r][c] = base
    for r, c in obj:
        out[r + drop][c + shift] = g[r][c]
    return out
