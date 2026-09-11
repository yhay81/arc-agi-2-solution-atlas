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


def paint(g, p, color):
    for r, c in p:
        if 0 <= r < len(g) and 0 <= c < len(g[0]):
            g[r][c] = color
    return g


def bg(g):
    return Counter(v for r in g for v in r).most_common(1)[0][0]


def solve(grid):
    g = grid
    b = bg(g)
    counts = Counter(v for row in g for v in row if v != b)
    outline = counts.most_common(1)[0][0]
    fill = counts.most_common()[-1][0] if len(counts) > 1 else 6
    a, bb, c, d = box(pts(g, outline))
    o = cp(g)
    paint(
        o, {(r, z) for r in range(a, bb + 1) for z in range(c, d + 1) if g[r][z] != outline}, fill
    )
    for r in range(a + 1, bb):
        if g[r][c] != outline:
            paint(o, {(r, z) for z in range(c)}, fill)
        if g[r][d] != outline:
            paint(o, {(r, z) for z in range(d + 1, len(g[0]))}, fill)
    for z in range(c + 1, d):
        if g[a][z] != outline:
            paint(o, {(r, z) for r in range(a)}, fill)
        if g[bb][z] != outline:
            paint(o, {(r, z) for r in range(bb + 1, len(g))}, fill)
    for r, z in product((a, bb), (c, d)):
        o[r][z] = g[r][z]
    return o
