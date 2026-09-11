from collections import Counter


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
    n = len(g) - 2
    panels = [[row[1 + j * (n + 1) : 1 + j * (n + 1) + n] for row in g[1:-1]] for j in range(4)]
    guide, one, two, _ = panels
    back = Counter(v for row in guide for v in row).most_common(1)[0][0]
    parts = components(guide, background=back, diagonal=True)
    mark = [ps for co, ps in parts if len(ps) == 1]
    if len(mark) != 1:
        raise ValueError("cannot separate the boundary marker from the region marker")
    seed = mark[0][0]
    wall = {(r, c) for co, ps in parts if len(ps) > 1 for r, c in ps}
    seen = {seed}
    q = [seed]
    while q:
        r, c = q.pop()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            p = (r + dr, c + dc)
            if 0 <= p[0] < n and 0 <= p[1] < n and (p not in wall) and (p not in seen):
                seen.add(p)
                q.append(p)
    for r in range(n):
        for c in range(n):
            p = (r, c)
            out[r + 1][1 + 3 * (n + 1) + c] = (
                one[r][c] if p in seen or (p in wall and one[r][c] != back) else two[r][c]
            )
    return out
