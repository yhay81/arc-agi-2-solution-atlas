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


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = cp(g)
    for obj in components(g, 0, False, True):
        a, b, c, d = bbox(obj)
        rowcounts = Counter((r for r, col in obj))
        colcounts = Counter((col for r, col in obj))
        rs = [r for r, n in rowcounts.items() if n == max(rowcounts.values())]
        cs = [c for c, n in colcounts.items() if n == max(colcounts.values())]
        cr, cc = ((min(rs) + max(rs)) / 2, (min(cs) + max(cs)) / 2)
        radius = max((abs(r - cr) + abs(col - cc) for r, col in obj))
        for r in range(len(g)):
            for col in range(len(g[0])):
                if abs(r - cr) + abs(col - cc) <= radius and g[r][col] == 0:
                    out[r][col] = 4
    return out
