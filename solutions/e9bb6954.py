def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = cp(g)
    h, w = (len(g), len(g[0]))
    seeds = []
    for r in range(h - 2):
        for c in range(w - 2):
            v = g[r][c]
            if v != 0 and all(g[r + dr][c + dc] == v for dr in range(3) for dc in range(3)):
                seeds.append((r + 1, c + 1, v))
    out = cp(g)
    for r in range(h):
        for c in range(w):
            hits = [color for a, b, color in seeds if a == r or b == c]
            if len(hits) > 1:
                out[r][c] = 0
            elif hits:
                out[r][c] = hits[0]
    return out
