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
    background = bg(g)
    objects = [(color, ps) for color, ps in components(g, background=background) if len(ps) >= 8]
    frames = [
        (col, [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == col])
        for col in set(v for row in g for v in row)
        if col != background
    ]
    frame = bbox(
        max(
            frames,
            key=lambda p: (bbox(p[1])[2] - bbox(p[1])[0] + 1) * (bbox(p[1])[3] - bbox(p[1])[1] + 1),
        )[1]
    )
    a, b, z, d = frame
    candidates = [
        (col, ps)
        for col, ps in objects
        if col != 7
        and a <= bbox(ps)[0] <= bbox(ps)[2] <= z
        and (b <= bbox(ps)[1] <= bbox(ps)[3] <= d)
    ]
    if len(candidates) != 1:
        raise ValueError("shape inside the broken frame is not unique")
    a, b, z, d = bbox(candidates[0][1])
    return [row[b : d + 1] for row in g[a : z + 1]]
