from collections import Counter


def bbox(ps):
    return (
        min((r for r, c in ps)),
        min((c for r, c in ps)),
        max((r for r, c in ps)),
        max((c for r, c in ps)),
    )


def components(g, background=None, by_color=True, diagonal=False):
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if diagonal:
        offsets += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    h, w = (len(g), len(g[0]))
    unseen = {(r, c) for r in range(h) for c in range(w) if g[r][c] != background}
    result = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        queue = [start]
        cells = []
        color = g[start[0]][start[1]]
        while queue:
            r, c = queue.pop()
            cells.append((r, c))
            for dr, dc in offsets:
                p = (r + dr, c + dc)
                if p in unseen and (not by_color or g[p[0]][p[1]] == color):
                    unseen.remove(p)
                    queue.append(p)
        result.append((color, cells))
    return result


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    back = bg(g)
    groups = components(g, background=back)
    color, ps = max(groups, key=lambda p: len(p[1]))
    a, b, z, d = bbox(ps)
    h, w = (z - a + 1, d - b + 1)
    markers = [(co, cs[0]) for co, cs in groups if len(cs) == 1]
    pivot = next((p for co, p in markers if co == color))
    other = next((co for co, p in markers if co != color))
    out = [[back] * len(g[0]) for _ in g]
    for co, (r, c) in markers:
        top = a + (r - pivot[0]) // 2 * h
        left = b + (c - pivot[1]) // 2 * w
        v = other if co == color else color
        for x, y in ps:
            rr, cc = (top + x - a, left + y - b)
            if 0 <= rr < len(g) and 0 <= cc < len(g[0]):
                out[rr][cc] = v
    return out
