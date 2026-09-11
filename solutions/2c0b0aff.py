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


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    crosses = {
        (r, c)
        for r, c in pts(g, 3)
        if all(((r + dr, c + dc) in pts(g, 3) for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]))
    }
    cands = []
    for p in cc(g, 0):
        if g[next(iter(p))[0]][next(iter(p))[1]] == 3:
            continue
        a, b, c, d = box(p)
        score = sum((a < r < b and c < z < d for r, z in crosses))
        if score:
            cands.append((score, p))
    return crop(g, max(cands, key=lambda x: x[0])[1])
