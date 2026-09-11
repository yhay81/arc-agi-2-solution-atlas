from itertools import combinations


def paint(g, p, color):
    for r, c in p:
        if 0 <= r < len(g) and 0 <= c < len(g[0]):
            g[r][c] = color
    return g


def pts(g, color):
    return {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color}


def line(a, b):
    dr = b[0] - a[0]
    dc = b[1] - a[1]
    n = max(abs(dr), abs(dc))
    return {a} if not n else {(a[0] + dr * i // n, a[1] + dc * i // n) for i in range(n + 1)}


def cp(g):
    return [list(r) for r in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    green = pts(g, 3)
    centers = [
        p
        for p in green
        if all(((p[0] + dr, p[1] + dc) in green for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]))
    ]
    o = cp(g)
    for a, b in combinations(centers, 2):
        if abs(a[0] - b[0]) == abs(a[1] - b[1]):
            paint(o, line(a, b), 2)
    return paint(o, green, 3)
