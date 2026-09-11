from collections import Counter
from itertools import product


def pts(g, color):
    return {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color}


def box(p):
    return (
        min((r for r, c in p)),
        max((r for r, c in p)),
        min((c for r, c in p)),
        max((c for r, c in p)),
    )


def cp(g):
    return [list(r) for r in g]


def cc(g, background=None, color=True, diag=False):
    if background is None:
        background = bg(g)
    rem = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != background}
    out = []
    while rem:
        start = min(rem)
        rem.remove(start)
        group = {start}
        q = [start]
        for r, c in q:
            for dr, dc in product((-1, 0, 1), repeat=2):
                if dr == dc == 0 or (not diag and abs(dr) + abs(dc) != 1):
                    continue
                p = (r + dr, c + dc)
                if p in rem and (not color or g[p[0]][p[1]] == g[r][c]):
                    rem.remove(p)
                    group.add(p)
                    q.append(p)
        out.append(group)
    return out


def paint(g, p, color):
    for r, c in p:
        if 0 <= r < len(g) and 0 <= c < len(g[0]):
            g[r][c] = color
    return g


def holes(g, p, background=0):
    a, b, c, d = box(p)
    h = b - a + 3
    w = d - c + 3
    mask = [[0] * w for _ in range(h)]
    for r, z in p:
        mask[r - a + 1][z - c + 1] = 1
    return [
        q for q in cc(mask, 1, False) if not any((r in (0, h - 1) or c in (0, w - 1) for r, c in q))
    ]


def bg(g):
    return Counter(v for r in g for v in r).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    objs = cc(g, 0)
    mapping = {}
    for p in objs:
        a, b, c, d = box(p)
        v = g[min(p)[0]][min(p)[1]]
        if v != 5 and min(b - a + 1, d - c + 1) == 3:
            mapping[len(holes(g, p))] = v
    if not (mapping):
        raise ValueError("task assumptions are not satisfied")
    o = cp(g)
    for p in objs:
        if p & pts(g, 5):
            paint(o, p, mapping.get(len(holes(g, p)), 0))
    return o
