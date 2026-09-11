from collections import Counter
from itertools import product


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
    o = [[0] * len(g[0]) for _ in g]
    objs.sort(key=lambda p: (not bool(holes(g, p)), box(p)[0] if holes(g, p) else -box(p)[1]))
    for p in objs:
        a, b, c, d = box(p)
        up = bool(holes(g, p))
        start = -a if up else len(g) - 1 - b
        direction = 1 if up else -1
        dr = start
        while any((o[r + dr][c] for r, c in p)):
            dr += direction
            if not all((0 <= r + dr < len(g) for r, c in p)):
                raise ValueError("No packing placement")
        for r, c in p:
            o[r + dr][c] = g[r][c]
    return o
