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
    background = bg(g)
    objects = components(g, background, False, False)
    tiles = []
    for obj in objects:
        a, b, c, d = bbox(obj)
        tiles.append([row[c : d + 1] for row in g[a : b + 1]])
    tiles.sort(key=lambda t: len(t) * len(t[0]), reverse=True)
    out = cp(tiles[0])
    for tile in tiles[1:]:
        shared = set(sum(tile, [])) & set(sum(out, []))
        ph, pw = (len(tile), len(tile[0]))
        candidates = []
        if not shared:
            raise ValueError("No matching anchor color")
        for a in range(len(out) - ph + 1):
            for c in range(len(out[0]) - pw + 1):
                if all(
                    (tile[r][col] if tile[r][col] in shared else None)
                    == (out[a + r][c + col] if out[a + r][c + col] in shared else None)
                    for r in range(ph)
                    for col in range(pw)
                ):
                    candidates.append((a, c))
        if len(candidates) != 1:
            raise ValueError(("Placement not unique", candidates))
        a, c = candidates[0]
        for r, row in enumerate(tile):
            out[a + r][c : c + pw] = row
    return out
