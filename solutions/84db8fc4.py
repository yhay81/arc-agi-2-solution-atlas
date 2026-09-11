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


def paint(g, p, color):
    for r, c in p:
        if 0 <= r < len(g) and 0 <= c < len(g[0]):
            g[r][c] = color
    return g


def cp(g):
    return [list(r) for r in g]


def bg(g):
    return Counter(v for r in g for v in r).most_common(1)[0][0]


def solve(grid):
    g = grid
    o = cp(g)
    mask = [[0 if v == 0 else 1 for v in row] for row in g]
    for p in cc(mask, 1, False):
        paint(
            o, p, 2 if any((r in (0, len(g) - 1) or c in (0, len(g[0]) - 1) for r, c in p)) else 5
        )
    return o
