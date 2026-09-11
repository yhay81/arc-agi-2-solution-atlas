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
    h, w = (len(g), len(g[0]))
    out = copy(g)
    rays = []
    for color, ps in components(g, 8):
        if color != 1:
            continue
        top, left, bottom, right = bbox(ps)
        sides = [
            (-1, 0, [(top, c) for c in range(left, right + 1) if g[top][c] == 1]),
            (1, 0, [(bottom, c) for c in range(left, right + 1) if g[bottom][c] == 1]),
            (0, -1, [(r, left) for r in range(top, bottom + 1) if g[r][left] == 1]),
            (0, 1, [(r, right) for r in range(top, bottom + 1) if g[r][right] == 1]),
        ]
        for dr, dc, edge in sides:
            strips = []
            k = 1
            while all(
                (
                    0 <= r + k * dr < h
                    and 0 <= c + k * dc < w
                    and (g[r + k * dr][c + k * dc] not in (1, 8))
                    for r, c in edge
                )
            ):
                strips.append([g[r + k * dr][c + k * dc] for r, c in edge])
                k += 1
            if strips:
                period = next(
                    n
                    for n in range(1, len(strips) + 1)
                    if all((row == strips[i % n] for i, row in enumerate(strips)))
                )
                rays.append((dr != 0, dr, dc, edge, strips[:period]))
    for _, dr, dc, edge, pattern in sorted(rays):
        k = 1
        while all((0 <= r + k * dr < h and 0 <= c + k * dc < w for r, c in edge)):
            for (r, c), v in zip(edge, pattern[(k - 1) % len(pattern)]):
                out[r + k * dr][c + k * dc] = v
            k += 1
    return out
