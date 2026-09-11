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
    mask = [[2 if v == 2 else 0 for v in row] for row in g]
    glyphs = components(mask, 0, False, True)
    glyphs.sort(key=lambda o: bbox(o)[2])
    out = [[0] * 7 for _ in range(8)]
    r, c = (0, 3)
    out[r][c] = 3
    for glyph in glyphs:
        a, b, left, right = bbox(glyph)
        shape = {(rr - a, cc - left) for rr, cc in glyph}
        r += 1
        out[r][c] = 2
        if shape == {(0, 0), (1, 0), (1, 1)}:
            c += 1
            out[r][c] = 2
        elif shape == {(0, 1), (1, 0), (1, 1)}:
            c -= 1
            out[r][c] = 2
        elif shape == {(0, 0), (1, 0)}:
            r += 1
            out[r][c] = 2
        else:
            raise ValueError("Unknown movement glyph")
    if r != 7:
        raise ValueError("Path does not end on bottom row")
    return out
