from collections import Counter


def cp(g):
    return [list(r) for r in g]


def paint(g, p, color):
    for r, c in p:
        if 0 <= r < len(g) and 0 <= c < len(g[0]):
            g[r][c] = color
    return g


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h = len(g)
    n = next(n for n in range(2, 6) if n * n + n - 1 == h)
    v = Counter(v for row in g for v in row if v).most_common(1)[0][0]
    o = cp(g)
    for i in range(n):
        for j in range(n):
            r, c = (i * (n + 1), j * (n + 1))
            paint(o, {(r + a, c + b) for a in range(n) for b in range(n)}, v)
            o[r + i][c + j] = 0
    return o
