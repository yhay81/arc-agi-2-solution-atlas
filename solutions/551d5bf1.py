def copy(g):
    return [r[:] for r in g]


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
    out = copy(g)
    h, w = (len(g), len(g[0]))
    for col, ps in components(g, 0):
        if col != 1:
            continue
        top, left, bottom, right = bbox(ps)
        for r in range(top + 1, bottom):
            for c in range(left + 1, right):
                out[r][c] = 8
        sides = [
            (-1, 0, [(top, c) for c in range(left + 1, right)]),
            (1, 0, [(bottom, c) for c in range(left + 1, right)]),
            (0, -1, [(r, left) for r in range(top + 1, bottom)]),
            (0, 1, [(r, right) for r in range(top + 1, bottom)]),
        ]
        for dr, dc, points in sides:
            for r, c in points:
                if g[r][c] == 0:
                    while 0 <= r < h and 0 <= c < w and (g[r][c] == 0):
                        out[r][c] = 8
                        r += dr
                        c += dc
    return out
