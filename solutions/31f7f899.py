from collections import Counter


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
    background = bg(g)
    axis = next(
        v
        for v in set(sum(g, [])) - {background}
        if any(all(x in (v,) or x != background for x in row) and row.count(v) > 0 for row in g)
        and any(row.count(v) >= len(row) // 3 for row in g)
    )
    guide = max(range(len(g)), key=lambda r: sum(v != background for v in g[r]))
    axis = Counter(g[guide]).most_common(1)[0][0]
    objects = components(
        [[0 if v in (axis, background) else v for v in row] for row in g], 0, False, True
    )
    objects.sort(key=lambda o: bbox(o)[2])
    heights = sorted(bbox(o)[1] - bbox(o)[0] + 1 for o in objects)
    out = [[background] * len(g[0]) for _ in g]
    out[guide] = [axis] * len(g[0])
    for obj, height in zip(objects, heights):
        a, b, c, d = bbox(obj)
        color = g[obj[0][0]][obj[0][1]]
        for r in range(guide - height // 2, guide - height // 2 + height):
            for col in range(c, d + 1):
                put(out, r, col, color)
    return out
