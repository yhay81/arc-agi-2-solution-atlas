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
    back = bg(g)
    groups = components(g, background=back)
    frames = []
    small = []
    for co, ps in groups:
        a, b, z, d = bbox(ps)
        if (
            z - a >= 3
            and d - b >= 5
            and all(
                g[r][c] == co
                for r in range(a, z + 1)
                for c in range(b, d + 1)
                if r in (a, z) or c in (b, d)
            )
        ):
            frames.append((co, a, b, z, d))
        else:
            small.append((co, ps))
    counts = Counter((co for co, ps in small))
    out = [[back] * len(g[0]) for _ in g]
    for co, a, b, z, d in frames:
        for r in range(a, z + 1):
            for c in range(b, d + 1):
                if r in (a, z) or c in (b, d):
                    out[r][c] = co
        for j in range(counts[co]):
            out[(a + z) // 2][d - 2 * (j + 1)] = co
    return out
