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


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = copy(g)
    objects = sorted(components(g, background=8, diagonal=True), key=lambda p: -len(p[1]))
    winner, ps = objects[0]
    a, b, z, d = bbox(ps)
    center = min(
        ((r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 8),
        key=lambda p: (
            sum((min((abs(p[0] - r) + abs(p[1] - c) for r, c in cs)) for co, cs in objects)),
            abs(p[0] - len(g) / 2) + abs(p[1] - len(g[0]) / 2),
        ),
    )
    for col, cs in objects[1:]:
        r, c = min(cs, key=lambda p: abs(p[0] - center[0]) + abs(p[1] - center[1]))
        out[r][c] = 8
    tip = min(ps, key=lambda p: abs(p[0] - center[0]) + abs(p[1] - center[1]))
    cy, cx = ((a + z) / 2, (b + d) / 2)
    if abs(cy - center[0]) > abs(cx - center[1]):
        r = a - 1 if cy < center[0] else z + 1
        for c in range(tip[1] - 1, tip[1] + 2):
            if 0 <= r < len(g) and 0 <= c < len(g[0]):
                out[r][c] = winner
    else:
        c = b - 1 if cx < center[1] else d + 1
        for r in range(tip[0] - 1, tip[0] + 2):
            if 0 <= r < len(g) and 0 <= c < len(g[0]):
                out[r][c] = winner
    return out
