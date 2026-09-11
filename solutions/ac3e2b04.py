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
    vertical = max(sum(row[c] == 2 for row in g) for c in range(len(g[0]))) / len(g) > max(
        sum(v == 2 for v in row) for row in g
    ) / len(g[0])
    if not vertical:
        return [list(row) for row in zip(*solve([list(row) for row in zip(*g)]))]
    rails = [c for c in range(len(g[0])) if sum(row[c] == 2 for row in g) > len(g) // 2]
    for color, ps in components(g, background=0):
        if color != 3:
            continue
        a, b, z, d = bbox(ps)
        r = (a + z) // 2
        for c in range(len(g[0])):
            if out[r][c] == 0:
                out[r][c] = 1
        for c in rails:
            if b <= c <= d:
                continue
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if 0 <= r + dr < len(g) and 0 <= c + dc < len(g[0]) and (dr or dc):
                        out[r + dr][c + dc] = 1
    return out
