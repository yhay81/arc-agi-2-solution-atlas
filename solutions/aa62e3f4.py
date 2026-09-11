from collections import Counter


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    back = bg(g)
    ps = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != back}
    color = Counter((g[r][c] for r, c in ps)).most_common()[-1][0]
    out = [[back] * len(g[0]) for _ in g]
    for r, c in ps:
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            a, b = (r + dr, c + dc)
            if 0 <= a < len(g) and 0 <= b < len(g[0]) and ((a, b) not in ps):
                out[a][b] = color
    return out
