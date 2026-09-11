from collections import Counter


def pts(g, color):
    return {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color}


def pal(g):
    return set(v for r in g for v in r)


def box(p):
    return (
        min((r for r, c in p)),
        max((r for r, c in p)),
        min((c for r, c in p)),
        max((c for r, c in p)),
    )


def bg(g):
    return Counter(v for r in g for v in r).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    b = bg(g)
    colors = pal(g) - {b}
    frames = {}
    edges = set()
    for v in colors:
        a, bb, c, d = box(pts(g, v))
        frames[v] = {
            (r, z) for r in range(a, bb + 1) for z in range(c, d + 1) if r in (a, bb) or z in (c, d)
        }
    for v, p in frames.items():
        for r, c in p:
            u = g[r][c]
            if u in colors and u != v:
                edges.add((v, u))
    order = []
    while colors:
        candidates = colors - {z for a, z in edges if a in colors and z in colors}
        if not (len(candidates) == 1):
            raise ValueError("task assumptions are not satisfied")
        v = candidates.pop()
        order.append(v)
        colors.remove(v)
    return [[v] for v in order]
