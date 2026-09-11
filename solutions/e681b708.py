from collections import Counter


def cp(g):
    return [row[:] for row in g]


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
    barriers = set()
    for r, row in enumerate(g):
        start = 0
        while start < w:
            end = start
            while end < w and row[end] == 1:
                end += 1
            if end - start >= 4 or (
                end - start >= 2
                and (
                    (start > 0 and row[start - 1] not in (0, 1))
                    or (end < w and row[end] not in (0, 1))
                )
            ):
                barriers.update((r, c) for c in range(start, end))
            start = max(end, start + 1)
    for c in range(w):
        start = 0
        while start < h:
            end = start
            while end < h and g[end][c] == 1:
                end += 1
            if end - start >= 4 or (
                end - start >= 2
                and (
                    (start > 0 and g[start - 1][c] not in (0, 1))
                    or (end < h and g[end][c] not in (0, 1))
                )
            ):
                barriers.update((r, c) for r in range(start, end))
            start = max(end, start + 1)
    barriers.update(
        ((r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v not in (0, 1))
    )
    mask = [[0 if (r, c) in barriers else 1 for c in range(w)] for r in range(h)]
    regions = components(mask, 0, False, True)
    out = cp(g)
    for region in regions:
        boundary = set(
            ((r + dr, c + dc) for r, c in region for dr in (-1, 0, 1) for dc in (-1, 0, 1))
        )
        counts = Counter(
            (g[r][c] for r, c in boundary if 0 <= r < h and 0 <= c < w and (g[r][c] not in (0, 1)))
        )
        if not counts:
            raise ValueError("Region has no color marks")
        color = counts.most_common(1)[0][0]
        for r, c in region:
            if g[r][c] == 1:
                out[r][c] = color
    return out
