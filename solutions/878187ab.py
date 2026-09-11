from collections import Counter


def paint(g, p, color):
    for r, c in p:
        if 0 <= r < len(g) and 0 <= c < len(g[0]):
            g[r][c] = color
    return g


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    counts = sorted(Counter(v for row in g for v in row if v != 7).values())
    if not (len(counts) == 2):
        raise ValueError("task assumptions are not satisfied")
    h, w = counts
    o = [[7] * 16 for _ in range(16)]
    paint(o, {(r, c) for r in range(16 - h, 16) for c in range(w)}, 2)
    for i in range(h):
        paint(o, {(15 - i, i), (15 - i, w - 1 - i)}, 4)
    return o
