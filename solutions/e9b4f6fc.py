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
    objects = components(g, background=0, by_color=False)
    large = max(objects, key=lambda p: len(p[1]))
    mapping = {}
    for color, ps in objects:
        if len(ps) == 2:
            (a, b), (c, d) = ps
            mapping[g[a][b]] = g[c][d]
            mapping[g[c][d]] = g[a][b]
    a, b, z, d = bbox(large[1])
    return [[mapping.get(v, v) for v in row[b : d + 1]] for row in g[a : z + 1]]
