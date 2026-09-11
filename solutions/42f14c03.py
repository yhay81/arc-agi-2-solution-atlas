import json as json
from collections import Counter


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


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    background = bg(g)
    groups = components(g, background)
    solutions = []
    for base, (color, ps) in enumerate(groups):
        top, left, bottom, right = bbox(ps)
        h, w = (bottom - top + 1, right - left + 1)
        holes = {(r, c) for r in range(h) for c in range(w) if (r + top, c + left) not in ps}
        if not holes:
            continue
        initial = [[background] * w for _ in range(h)]
        for r, c in ps:
            initial[r - top][c - left] = color
        pieces = []
        for i, (col, other) in enumerate(groups):
            if i == base or len(other) > len(holes):
                continue
            a, b, z, d = bbox(other)
            pieces.append((i, col, [(r - a, c - b) for r, c in other]))

        def fill(remain, used, out):
            if not remain:
                solutions.append(out)
                return
            first = min(remain)
            for i, col, shape in pieces:
                if i in used:
                    continue
                for pr, pc in shape:
                    dr, dc = (first[0] - pr, first[1] - pc)
                    placed = {(r + dr, c + dc) for r, c in shape}
                    if placed <= remain:
                        nxt = copy(out)
                        for r, c in placed:
                            nxt[r][c] = col
                        fill(remain - placed, used | {i}, nxt)

        fill(holes, set(), initial)
    unique = {json.dumps(x): x for x in solutions}
    if len(unique) != 1:
        raise ValueError(f"there are {len(unique)} rectangle-completion candidates")
    return next(iter(unique.values()))
