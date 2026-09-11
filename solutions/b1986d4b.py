from collections import Counter


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


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    base = bg(g)
    counts = {}
    sizes = {}
    for obj in components(g, base, False, True):
        a, b, c, d = bbox(obj)
        size = b - a + 1
        if size >= 2 and size == d - c + 1 and (len(obj) == size * size):
            color = g[obj[0][0]][obj[0][1]]
            counts[color] = counts.get(color, 0) + 1
            sizes[color] = size
    largest = max(sizes.values())
    largest_count = sum(counts[c] for c in counts if sizes[c] == largest)
    groups = []
    for i in range(min(max(counts.values()), 2 * largest_count)):
        active = [c for c in counts if counts[c] > i]
        width = max(sizes[c] for c in active) + 1
        groups.append((active, width))
    out = [[base] * sum((w for a, w in groups)) for _ in range(max(sizes.values()) + 1)]
    offset = 0
    for active, width in groups:
        for color in sorted(active, key=lambda c: sizes[c], reverse=True):
            for r in range(sizes[color]):
                for c in range(sizes[color]):
                    out[r][offset + c] = color
        offset += width
    return out
