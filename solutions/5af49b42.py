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
    g = copy(g)
    out = copy(g)
    obs = components(g, 0, False)
    patterns = [ps for col, ps in obs if len(ps) > 1]
    for col, ps in obs:
        if len(ps) != 1:
            continue
        r, c = ps[0]
        matches = [(shape, (a, b)) for shape in patterns for a, b in shape if g[a][b] == col]
        if len(matches) != 1:
            raise ValueError("template containing the signal color is not unique")
        shape, (a, b) = matches[0]
        for x, y in shape:
            if 0 <= x + r - a < len(g) and 0 <= y + c - b < len(g[0]):
                out[x + r - a][y + c - b] = g[x][y]
    return out
