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
    objects = [(g[o[0][0]][o[0][1]], bbox(o)) for o in components(g, 0, False, True)]
    edges = []
    for i, (color, (a, b, c, d)) in enumerate(objects):
        for j, (v, (aa, bb, cc, dd)) in enumerate(objects):
            if color != v:
                continue
            if cc > d and max(a, aa) + 1 < min(b, bb):
                edges.append(
                    (
                        cc - d - 1,
                        i,
                        j,
                        [
                            (r, col)
                            for r in range(max(a, aa) + 1, min(b, bb))
                            for col in range(d + 1, cc)
                        ],
                    )
                )
            if aa > b and max(c, cc) + 1 < min(d, dd):
                edges.append(
                    (
                        aa - b - 1,
                        i,
                        j,
                        [
                            (r, col)
                            for r in range(b + 1, aa)
                            for col in range(max(c, cc) + 1, min(d, dd))
                        ],
                    )
                )
    parent = list(range(len(objects)))

    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i

    for gap, i, j, pts in sorted(edges):
        if find(i) == find(j):
            continue
        parent[find(i)] = find(j)
        for r, c in pts:
            if g[r][c] == 0:
                out[r][c] = 8
    return out
