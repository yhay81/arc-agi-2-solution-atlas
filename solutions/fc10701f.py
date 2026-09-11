from collections import Counter


def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = cp(g)
    base = bg(g)
    source = points(g, 7)
    target = points(g, 9)
    a, b, c, d = bbox(source)
    aa, bb, cc, dd = bbox(target)
    for r, col in source:
        out[r][col] = base
    if c == cc:
        for r in range(min(a, aa), max(b, bb) + 1):
            if c > 0 and d + 1 < len(g[0]) and (g[r][c - 1] == g[r][d + 1] == 0):
                for col in range(c, d + 1):
                    out[r][col] = 2
    else:
        for col in range(min(c, cc), max(d, dd) + 1):
            if a > 0 and b + 1 < len(g) and (g[a - 1][col] == g[b + 1][col] == 0):
                for r in range(a, b + 1):
                    out[r][col] = 2
    for r, col in target:
        out[r][col] = 7
    return out
