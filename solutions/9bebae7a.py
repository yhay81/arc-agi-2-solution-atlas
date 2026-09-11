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


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = [[0 if v == 6 else v for v in row] for row in g]
    ps = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 4]
    a, b, z, d = bbox(ps)
    mark = [p for color, cs in components(g, background=0) if color == 6 for p in cs]
    t, l, u, q = bbox(mark)
    row = Counter((r for r, c in mark)).most_common(1)[0][0]
    col = Counter((c for r, c in mark)).most_common(1)[0][0]
    if row == t:
        dr, dc = (0, 1)
    elif row == u:
        dr, dc = (0, -1)
    elif col < (l + q) / 2:
        dr, dc = (-1, 0)
    else:
        dr, dc = (1, 0)
    for r, c in ps:
        rr = 2 * z + 1 - r if dr == 1 else 2 * a - 1 - r if dr == -1 else r
        cc = 2 * d + 1 - c if dc == 1 else 2 * b - 1 - c if dc == -1 else c
        if 0 <= rr < len(g) and 0 <= cc < len(g[0]):
            out[rr][cc] = 4
    return out
