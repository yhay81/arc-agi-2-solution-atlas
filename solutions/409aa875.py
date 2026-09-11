from collections import Counter


def copy(g):
    return [r[:] for r in g]


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
    out = copy(g)
    groups = components(g, background=back, diagonal=True)
    hits = Counter()
    for color, ps in groups:
        if len(ps) != 3:
            continue
        apex = min(ps, key=lambda p: sum((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 for q in ps))
        others = [p for p in ps if p != apex]
        dr = 2 * apex[0] - sum(p[0] for p in others)
        dc = 2 * apex[1] - sum(p[1] for p in others)
        dr = (dr > 0) - (dr < 0)
        dc = (dc > 0) - (dc < 0)
        r, c = (apex[0] + 5 * dr, apex[1] + 5 * dc)
        if 0 <= r < len(g) and 0 <= c < len(g[0]):
            hits[r, c] += 1
    for color, ps in groups:
        if any(p in hits for p in ps):
            for r, c in ps:
                out[r][c] = 9
    for (r, c), count in hits.items():
        out[r][c] = 1 if count > 1 else 9
    return out
