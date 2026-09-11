from collections import Counter


def box(p):
    return (
        min((r for r, c in p)),
        max((r for r, c in p)),
        min((c for r, c in p)),
        max((c for r, c in p)),
    )


def cp(g):
    return [list(r) for r in g]


def bg(g):
    return Counter(v for r in g for v in r).most_common(1)[0][0]


def crop(g, p):
    a, b, c, d = box(p)
    return [row[c : d + 1] for row in g[a : b + 1]]


def solve(grid):
    g = grid
    g = cp(g)
    b = bg(g)
    p = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != b}
    a, bb, c, d = box(p)
    tile = crop(g, p)
    o = cp(g)
    x = d + 1
    scale = 2
    center = (a + bb + 1) / 2
    while x < len(g[0]):
        h = len(tile) * scale
        top = round(center - h / 2)
        for r in range(h):
            for z in range(len(tile[0]) * scale):
                if 0 <= top + r < len(g) and x + z < len(g[0]):
                    o[top + r][x + z] = tile[r // scale][z // scale]
        x += len(tile[0]) * scale
        scale *= 2
    return o
