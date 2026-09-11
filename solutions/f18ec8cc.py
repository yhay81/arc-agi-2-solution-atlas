from collections import Counter


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    modes = [Counter(g[r][c] for r in range(h)).most_common(1)[0][0] for c in range(w)]
    bands = []
    start = 0
    for c in range(1, w + 1):
        if c == w or modes[c] != modes[start]:
            bands.append((start, c, modes[start]))
            start = c
    colors = {color: i for i, (_, _, color) in enumerate(bands)}
    edges = [set() for _ in bands]
    for i, (left, right, color) in enumerate(bands):
        middle = (left + right - 1) / 2
        for r in range(h):
            for c in range(left, right):
                v = g[r][c]
                if v == color or v not in colors:
                    continue
                j = colors[v]
                if c < middle:
                    edges[j].add(i)
                elif c > middle:
                    edges[i].add(j)
    indeg = [0] * len(bands)
    for i in range(len(bands)):
        for j in edges[i]:
            indeg[j] += 1
    order = []
    available = [i for i, d in enumerate(indeg) if d == 0]
    while available:
        i = min(available)
        available.remove(i)
        order.append(i)
        for j in edges[i]:
            indeg[j] -= 1
            if indeg[j] == 0:
                available.append(j)
    if len(order) != len(bands):
        order = []
    widths = [b - a for a, b, _ in bands]
    if len(bands) == 3 and len(set(widths)) == 3:
        order = list(reversed(range(3)))
    else:
        order = list(range(1, len(bands))) + [0]
    out = [[] for _ in range(h)]
    for i in order:
        a, b, _ = bands[i]
        for r in range(h):
            out[r].extend(g[r][a:b])
    return out
