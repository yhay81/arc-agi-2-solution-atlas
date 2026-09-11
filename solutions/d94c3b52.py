from collections import Counter
from itertools import combinations, product


def pts(g, color):
    return {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color}


def norm(p):
    a, b, c, d = box(p)
    return {(r - a, c - c0) for r, c0 in []} if False else {(r - a, z - c) for r, z in p}


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
    objs = cc(g, 0, True, True)
    refs = [p for p in objs if p & pts(g, 8)]
    if not (refs):
        raise ValueError("task assumptions are not satisfied")
    pattern = norm(refs[0])
    targets = [p for p in objs if norm(p) == pattern]
    o = cp(g)
    centers = [((box(p)[0] + box(p)[1]) / 2, (box(p)[2] + box(p)[3]) / 2) for p in targets]
    for p in objs:
        a, b, c, d = box(p)
        r, z = ((a + b) / 2, (c + d) / 2)
        if p in targets:
            paint(o, p, 8)
        elif any(
            (
                (u[0] == v[0] == r and min(u[1], v[1]) < z < max(u[1], v[1]))
                or (u[1] == v[1] == z and min(u[0], v[0]) < r < max(u[0], v[0]))
                for u, v in combinations(centers, 2)
            )
        ):
            paint(o, p, 7)
    return o
