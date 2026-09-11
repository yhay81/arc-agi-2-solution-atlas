from collections import Counter
from itertools import product


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


def crop(g, p):
    a, b, c, d = box(p)
    return [row[c : d + 1] for row in g[a : b + 1]]


def bg(g):
    return Counter(v for r in g for v in r).most_common(1)[0][0]


def box(p):
    return (
        min((r for r, c in p)),
        max((r for r, c in p)),
        min((c for r, c in p)),
        max((c for r, c in p)),
    )


def solve(grid):
    g = grid
    b = bg(g)
    objs = cc(g, b, False, True)
    groups = {}
    for p in objs:
        tile = crop(g, p)
        key = tuple(tuple(row) for row in tile)
        groups.setdefault(key, []).append(p)
    key = max(groups, key=lambda k: len(groups[k]))
    return [list(row) for row in key]
