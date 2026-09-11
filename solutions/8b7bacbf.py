from collections import Counter
from itertools import product


def pts(g, color):
    return {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color}


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
    background = bg(g)
    counts = Counter(v for row in g for v in row)
    seeds = [v for v, n in counts.items() if v != background and n == 1]
    o = cp(g)
    h, w = (len(g), len(g[0]))
    rings = []
    for p in cc([[0 if v == background else 1 for v in row] for row in g], 1, False):
        border = {
            (r + dr, c + dc)
            for r, c in p
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]
            if 0 <= r + dr < h and 0 <= c + dc < w and (g[r + dr][c + dc] != background)
        }
        colors = {g[r][c] for r, c in border}
        if len(colors) == 1:
            rings.append((p, border))
    for v in seeds:
        seed = next(iter(pts(g, v)))
        r, c = seed
        adj = [
            g[r + dr][c + dc]
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]
            if 0 <= r + dr < h and 0 <= c + dc < w and (g[r + dr][c + dc] != background)
        ]
        if not adj:
            continue
        col = Counter(adj).most_common(1)[0][0]
        own = pts(g, col)
        ringpoints = set().union(*(border for p, border in rings))
        hidden = {
            (r, c)
            for r, row in enumerate(g)
            for c, x in enumerate(row)
            if x not in (background, col)
            and (r, c) not in ringpoints
            and (sum(((r + dr, c + dc) in own for dr, dc in product((-1, 0, 1), repeat=2))) >= 2)
        }
        mask = [[col if (r, c) in own | hidden else background for c in range(w)] for r in range(h)]
        wires = cc(mask, background, True, True)
        expanded = [
            {(r + dr, c + dc) for r, c in q for dr, dc in product((-1, 0, 1), repeat=2)}
            for q in wires
        ]
        active = {i for i, p in enumerate(expanded) if seed in p}
        filled = set()
        change = True
        while change:
            change = False
            for j, (p, border) in enumerate(rings):
                if j not in filled and any(border & expanded[i] for i in active):
                    filled.add(j)
                    change = True
            for i, q in enumerate(expanded):
                if i not in active and any(q & rings[j][1] for j in filled):
                    active.add(i)
                    change = True
        for j in filled:
            paint(o, rings[j][0], v)
    return o
