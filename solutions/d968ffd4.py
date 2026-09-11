from collections import Counter


def bbox(ps):
    return (
        min((r for r, c in ps)),
        min((c for r, c in ps)),
        max((r for r, c in ps)),
        max((c for r, c in ps)),
    )


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
    if len(g) > len(g[0]):
        t = [list(row) for row in zip(*g)]
        return [list(row) for row in zip(*solve(t))]
    out = copy(g)
    background = bg(g)
    objects = sorted(components(g, background=background), key=lambda p: bbox(p[1])[1])
    (one, ps), (two, qs) = objects
    a, b, z, d = bbox(ps)
    e, f, x, y = bbox(qs)
    w = len(g[0])
    for r in range(len(g)):
        for c in range(d + 1, w // 2):
            out[r][c] = one
        for c in range((w + 1) // 2, f):
            out[r][c] = two
    return out
