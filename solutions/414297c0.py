def bounds(points):
    return (
        min(r for r, _ in points),
        min(c for _, c in points),
        max(r for r, _ in points),
        max(c for _, c in points),
    )


def components(mask, diagonal=False):
    unseen = {(r, c) for r, row in enumerate(mask) for c, value in enumerate(row) if value}
    result = []
    offsets = [
        (dr, dc)
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if (dr or dc) and (diagonal or not (dr and dc))
    ]
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        q = [start]
        cells = []
        while q:
            r, c = q.pop()
            cells.append((r, c))
            for dr, dc in offsets:
                p = (r + dr, c + dc)
                if p in unseen:
                    unseen.remove(p)
                    q.append(p)
        result.append(cells)
    return result


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    objs = components([[v != 0 for v in row] for row in a], True)
    main = max(objs, key=len)
    r, c, b, d = bounds(main)
    out = [row[c : d + 1] for row in a[r : b + 1]]
    for ps in objs:
        if ps is main:
            continue
        colors = {a[y][x] for y, x in ps} - {2}
        if not (len(colors) == 1):
            raise ValueError("task assumptions are not satisfied")
        marker = colors.pop()
        src = next(p for p in ps if a[p[0]][p[1]] == marker)
        for dst in [
            (y, x) for y, row in enumerate(out) for x, value in enumerate(row) if value == marker
        ]:
            for y, x in ps:
                yy, xx = y - src[0] + dst[0], x - src[1] + dst[1]
                if 0 <= yy < len(out) and 0 <= xx < len(out[0]):
                    out[yy][xx] = a[y][x]
    return out
