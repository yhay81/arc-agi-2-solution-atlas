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
    out = [[8 if v == 3 else v for v in row] for row in g]
    for obj in components([[7 if v == 7 else 0 for v in row] for row in g], 0, False, True):
        a, b, c, d = bbox(obj)
        if a != b or d - c != 2:
            raise ValueError("Expected orange 3-bar")
        for col in range(c, d + 1):
            out[a][col] = 8
        for r in range(a - 1, a + 2):
            put(out, r, c + 1, 6)
    for region in components([[1 if v == 8 else 0 for v in row] for row in out], 0, False, True):
        seeds = [p for p in region if g[p[0]][p[1]] == 3]
        if not seeds:
            continue
        bottom = max((r for r, c in region))
        cells = sorted(((r, c) for r, c in region if r == bottom))
        above = [c for r, c in region if r == bottom - 1 and (bottom, c) in region]
        if (above and sum(above) / len(above) < (cells[0][1] + cells[-1][1]) / 2) or (
            not above and sum((c for r, c in seeds)) / len(seeds) >= (len(g[0]) - 1) / 2
        ):
            cells = cells[::-1]
        for r, c in cells[: len(seeds)]:
            out[r][c] = 3
    return out
