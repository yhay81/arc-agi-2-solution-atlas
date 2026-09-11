from collections import Counter


def mode(values):
    flat = (
        [v for item in values for v in item] if values and isinstance(values[0], list) else values
    )
    return Counter(flat).most_common(1)[0][0]


def bounds(points):
    return (
        min(r for r, _ in points),
        min(c for _, c in points),
        max(r for r, _ in points),
        max(c for _, c in points),
    )


def components(mask, diagonal=False):
    unseen = {(r, c) for r, row in enumerate(mask) for c, v in enumerate(row) if v}
    out = []
    offsets = [
        (dr, dc)
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if (dr or dc) and (diagonal or not (dr and dc))
    ]
    while unseen:
        p = min(unseen)
        unseen.remove(p)
        q = [p]
        cells = []
        while q:
            r, c = q.pop()
            cells.append((r, c))
            for dr, dc in offsets:
                n = (r + dr, c + dc)
                if n in unseen:
                    unseen.remove(n)
                    q.append(n)
        out.append(cells)
    return out


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    bg = mode(a)
    co = mode([v for row in a for v in row if v != bg])
    cs = components([[v == co for v in row] for row in a], False)
    rects = []
    for p in sorted(cs, key=lambda p: min(c for _, c in p)):
        r, c, b, d = bounds(p)
        if not (len(p) == (b - r + 1) * (d - c + 1)):
            raise ValueError("task assumptions are not satisfied")
        rects.append((b - r + 1, d - c + 1))
    width = sum((max(h, w) for h, w in rects)) + len(rects) - 1
    out = [[bg] * width for _ in range(10)]
    x = 0
    for h, w in rects:
        h, w = (min(h, w), max(h, w))
        for r in range(h):
            for c in range(x, x + w):
                out[r][c] = co
        x += w + 1
    x = 0
    for h, w in rects:
        h, w = (max(h, w), min(h, w))
        for r in range(10 - h, 10):
            for c in range(x, x + w):
                out[r][c] = co
        x += w + 1
    return out
