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
    h, w = (len(g), len(g[0]))
    bars = components([[2 if v == 2 else 0 for v in row] for row in g], 0, False, True)
    boxes = [bbox(o) for o in bars]
    for c in [c for c, v in enumerate(g[0]) if v == 8]:
        r = 0
        seen = set()
        while r < h:
            if (r, c) in seen:
                raise ValueError("Loop")
            seen.add((r, c))
            out[r][c] = 8
            if r + 1 < h and g[r + 1][c] == 2:
                box = next(
                    (box for box in boxes if box[0] <= r + 1 <= box[1] and box[2] <= c <= box[3]),
                    None,
                )
                a, b, left, right = box
                target = left - 1 if c - left < right - c else right + 1
                if not 0 <= target < w:
                    raise ValueError("Blocked escape")
                for col in range(min(c, target), max(c, target) + 1):
                    out[r][col] = 8
                c = target
            r += 1
    return out
