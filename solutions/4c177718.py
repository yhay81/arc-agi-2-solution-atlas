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
    sep = next((r for r, row in enumerate(g) if all(v == 5 for v in row)))
    out = copy(g[sep + 1 :])
    query = [(r, c) for r, row in enumerate(out) for c, v in enumerate(row) if v]
    top, left, bottom, right = bbox(query)
    header = g[:sep]
    objects = sorted(
        [ps for col, ps in components(header, 0, False, True)],
        key=lambda ps: min((c for r, c in ps)),
    )
    if len(objects) != 3:
        raise ValueError("legend does not contain exactly three symbols")
    direction = objects[1]
    a, b, d, e = bbox(direction)
    down = sum(g[a][c] != 0 for c in range(b, e + 1)) > sum(g[d][c] != 0 for c in range(b, e + 1))
    shape = objects[2]
    a, b, d, e = bbox(shape)
    start = bottom + 1 if down else top - (d - a + 1)
    for r, c in shape:
        x, y = (start + r - a, left + c - b)
        if 0 <= x < len(out) and 0 <= y < len(out[0]):
            out[x][y] = g[r][c]
    return out
