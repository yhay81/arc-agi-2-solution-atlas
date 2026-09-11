def paint(g, p, color):
    for r, c in p:
        if 0 <= r < len(g) and 0 <= c < len(g[0]):
            g[r][c] = color
    return g


def line(a, b):
    dr = b[0] - a[0]
    dc = b[1] - a[1]
    n = max(abs(dr), abs(dc))
    return {a} if not n else {(a[0] + dr * i // n, a[1] + dc * i // n) for i in range(n + 1)}


def cp(g):
    return [list(r) for r in g]


def solve(grid):
    g = grid
    o = cp(g)
    h, w = (len(g), len(g[0]))
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            if v:
                paint(
                    o,
                    line((r, c), (0 if r < h / 2 else h - 1, c))
                    | line((r, c), (r, 0 if c < w / 2 else w - 1)),
                    v,
                )
    return o
