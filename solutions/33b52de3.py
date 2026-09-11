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
    pts = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v not in (0, 5)]
    top, left, bottom, right = bbox(pts)
    legend = [row[left : right + 1] for row in g[top : bottom + 1]]
    obs = [ps for col, ps in components(g, 0) if col == 5]
    rows = sorted({min((r for r, c in ps)) for ps in obs})
    cols = sorted({min((c for r, c in ps)) for ps in obs})
    for ps in obs:
        a, b, _, _ = bbox(ps)
        col = legend[rows.index(a)][cols.index(b)]
        for r, c in ps:
            out[r][c] = col
    return out
