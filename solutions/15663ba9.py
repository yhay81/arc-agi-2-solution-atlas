from collections import Counter
from itertools import product


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
    b = bg(g)
    o = cp(g)
    for p in cc(g, b):
        hs = holes(g, p, b)
        a, bb, c, d = box(p)
        inside = {(r + a - 1, z + c - 1) for q in hs for r, z in q}
        for r, z in p:
            ns = [
                (dr, dc) for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)] if (r + dr, z + dc) in p
            ]
            if len(ns) == 2 and ns[0][0] != -ns[1][0]:
                dr = ns[0][0] + ns[1][0]
                dc = ns[0][1] + ns[1][1]
                o[r][z] = 4 if (r + dr, z + dc) in inside else 2
    return o
