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
    out = [[0] * len(g[0]) for _ in g]
    for _, ps in components(g, 0, False):
        top, left, bottom, right = bbox(ps)
        local = [
            [9 if g[r][c] == 9 else 0 for c in range(left, right + 1)]
            for r in range(top, bottom + 1)
        ]
        parts = components(local, 0)
        if len(parts) != 2:
            raise ValueError("the brown shape is not split into two parts at the gap")
        vertical = bottom - top > right - left
        parts.sort(key=lambda x: sum(p[0] if vertical else p[1] for p in x[1]) / len(x[1]))
        for j, (_, cells) in enumerate(parts):
            dr = 2 * j - 1 if vertical else 0
            dc = 0 if vertical else 2 * j - 1
            for r, c in cells:
                if 0 <= r + top + dr < len(g) and 0 <= c + left + dc < len(g[0]):
                    out[r + top + dr][c + left + dc] = 9
    return out
