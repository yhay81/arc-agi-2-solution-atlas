from collections import Counter
from itertools import product


def pal(g):
    return set(v for r in g for v in r)


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


def bg(g):
    return Counter(v for r in g for v in r).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    o = cp(g)
    for v in pal(g) - {g[0][0]}:
        for p in cc([[v if x == v else -1 for x in row] for row in g], -1):
            a, b, c, d = box(p)
            if b - a < 2 or d - c < 2:
                continue
            if not all(
                g[r][z] == v
                for r in range(a, b + 1)
                for z in range(c, d + 1)
                if r in (a, b) or z in (c, d)
            ):
                continue
            vertical = b - a > d - c
            for cross in range(c + 1, d) if vertical else range(a + 1, b):
                places = (
                    [(r, cross) for r in range(a + 1, b)]
                    if vertical
                    else [(cross, z) for z in range(c + 1, d)]
                )
                values = [g[r][z] for r, z in places]
                best = None
                for period in range(1, min(6, len(values)) + 1):
                    buckets = [Counter(values[i::period]) for i in range(period)]
                    tile = [co.most_common(1)[0][0] for co in buckets]
                    mismatch = sum(values[i] != tile[i % period] for i in range(len(values)))
                    score = (mismatch, period)
                    if best is None or score < best[0]:
                        best = (score, tile)
                tile = best[1]
                for i, (r, z) in enumerate(places):
                    o[r][z] = tile[i % len(tile)]
    return o
