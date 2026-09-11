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
    for color, ps in sorted(components(g, 7), key=lambda x: x[0], reverse=True):
        if color not in (2, 5) or len(ps) != 3:
            continue
        top, left, bottom, right = bbox(ps)
        if bottom - top != 1 or right - left != 1:
            raise ValueError("shape is not an L")
        missing = next(
            (r, c)
            for r in range(top, bottom + 1)
            for c in range(left, right + 1)
            if (r, c) not in ps
        )
        corner = (top + bottom - missing[0], left + right - missing[1])
        sign = 1 if color == 5 else -1
        dr = (missing[0] - corner[0]) * sign
        dc = (missing[1] - corner[1]) * sign
        for r, c in ps:
            if 0 <= r + dr < len(g) and 0 <= c + dc < len(g[0]):
                out[r + dr][c + dc] = 4 if color == 5 else 3
    return out
