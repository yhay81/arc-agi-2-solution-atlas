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
    obs = components(g, 0, False)
    obs.sort(key=lambda x: len(x[1]), reverse=True)
    target = obs[0][1]
    top, left, bottom, right = bbox(target)
    h, w = (bottom - top + 1, right - left + 1)
    background = g[top][left]
    refs = sorted([p for c, p in obs[1:]], key=lambda p: min((c for r, c in p)))
    if len(refs) != 2:
        raise ValueError("cannot separate the template from the placement map")
    a, b, d, e = bbox(refs[0])
    seed = [row[b : e + 1] for row in g[a : d + 1]]
    a, b, d, e = bbox(refs[1])
    layout = [row[b : e + 1] for row in g[a : d + 1]]
    color = next(
        iter(({g[r][c] for r, c in refs[0]} & {g[r][c] for r, c in refs[1]}) - {background})
    )
    ph, pw = (len(seed), len(seed[0]))
    nr, nc = (h // ph, w // pw)
    out = [[background] * w for _ in range(h)]
    for i in range(nr):
        for j in range(nc):
            if layout[i * len(layout) // nr][j * len(layout[0]) // nc] == color:
                for r in range(ph):
                    for c in range(pw):
                        if seed[r][c] == color:
                            out[i * ph + r][j * pw + c] = color
    return out
