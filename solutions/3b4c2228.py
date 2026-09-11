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
    n = sum(
        (
            color == 3
            and len(ps) == 4
            and (bbox(ps)[2] - bbox(ps)[0] == bbox(ps)[3] - bbox(ps)[1] == 1)
            for color, ps in components(g, 0)
        )
    )
    return [[int(r == c and r < n) for c in range(3)] for r in range(3)]
