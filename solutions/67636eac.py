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
    obs = [ps for col, ps in components(g, 0, False, True)]
    boxes = [bbox(ps) for ps in obs]
    vertical = max(b[0] for b in boxes) - min(b[0] for b in boxes) > max(b[1] for b in boxes) - min(
        b[1] for b in boxes
    )
    boxes.sort(key=lambda b: b[0] if vertical else b[1])
    tiles = [[row[b[1] : b[3] + 1] for row in g[b[0] : b[2] + 1]] for b in boxes]
    return (
        [row for tile in tiles for row in tile]
        if vertical
        else [[v for tile in tiles for v in tile[r]] for r in range(len(tiles[0]))]
    )
