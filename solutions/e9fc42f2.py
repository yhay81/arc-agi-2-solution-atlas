from collections import Counter
from itertools import product


def box(p):
    return (
        min((r for r, c in p)),
        max((r for r, c in p)),
        min((c for r, c in p)),
        max((c for r, c in p)),
    )


def shift(p, dr, dc):
    return {(r + dr, c + dc) for r, c in p}


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
    objs = cc(g, 2, False)
    if not (objs):
        raise ValueError("task assumptions are not satisfied")
    placed = {p: g[p[0]][p[1]] for p in objs[0]}
    remaining = objs[1:]
    while remaining:
        options = []
        for i, obj in enumerate(remaining):
            for a in obj:
                v = g[a[0]][a[1]]
                if v in (1, 2):
                    continue
                for b, col in placed.items():
                    if col != v:
                        continue
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        moved = shift(obj, b[0] + dr - a[0], b[1] + dc - a[1])
                        if moved & placed.keys():
                            continue
                        aa, bb, c, d = box(set(placed) | moved)
                        options.append(
                            ((bb - aa + 1) * (d - c + 1), i, b[0] + dr - a[0], b[1] + dc - a[1])
                        )
        if not (options):
            raise ValueError("task assumptions are not satisfied")
        _, i, dr, dc = min(options)
        obj = remaining.pop(i)
        for r, c in obj:
            placed[(r + dr, c + dc)] = g[r][c]
    a, b, c, d = box(placed)
    return [[placed.get((r, z), 2) for z in range(c, d + 1)] for r in range(a, b + 1)]
