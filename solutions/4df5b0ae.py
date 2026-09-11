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


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = [[7] * len(g[0]) for _ in g]
    perimeter = {
        (r, c)
        for r in range(len(g))
        for c in range(len(g[0]))
        if r in (0, len(g) - 1) or c in (0, len(g[0]) - 1)
    }
    objects = [(col, ps) for col, ps in components(g, 7) if set(ps) != perimeter]
    objects.sort(key=lambda x: len(x[1]))
    offset = 0
    for col, ps in objects:
        top, left, bottom, right = bbox(ps)
        for r, c in ps:
            out[len(g) - 1 - bottom + r][offset + c - left] = col
        offset += right - left + 1
    return out
