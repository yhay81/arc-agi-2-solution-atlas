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


def bg(g):
    return Counter(v for r in g for v in r).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    o = cp(g)
    for p in cc(g, 0):
        if not p & pts(g, 5):
            continue
        a, b, c, d = box(p)
        for r, z in [(a - 1, c - 1), (a - 1, d + 1), (b + 1, c - 1), (b + 1, d + 1)]:
            if not (0 <= r < len(g) and 0 <= z < len(g[0])):
                raise ValueError("task assumptions are not satisfied")
            v = g[r][z]
            if not (v not in (0, 5)):
                raise ValueError("task assumptions are not satisfied")
            o[r][z] = 0
            rr = range(a, (a + b + 1) // 2) if r < a else range((a + b + 1) // 2, b + 1)
            cs = range(c, (c + d + 1) // 2) if z < c else range((c + d + 1) // 2, d + 1)
            paint(o, set(product(rr, cs)), v)
    return o
