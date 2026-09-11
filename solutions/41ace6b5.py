from collections import Counter


def cp(g):
    return [row[:] for row in g]


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def solve(grid):
    g = grid
    out = cp(g)
    h, w = (len(g), len(g[0]))
    level = max(range(h), key=lambda r: g[r].count(5))
    common_cyan = Counter(
        sum(g[r][c] == 8 for r in range(h)) for c in range(w) if any(g[r][c] == 1 for r in range(h))
    ).most_common(1)[0][0]
    for c in range(w):
        blue = sum(g[r][c] == 1 for r in range(h))
        cyan = common_cyan
        if not blue:
            continue
        for r in range(h):
            out[r][c] = 7
        for r in range(level - cyan, level):
            put(out, r, c, 8)
        for r in range(level, level + blue):
            put(out, r, c, 1)
        for r in range(level + blue, h):
            out[r][c] = 9
    return out
