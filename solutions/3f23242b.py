def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = cp(g)
    for r, c in points(g, 3):
        for col in range(len(g[0])):
            put(out, r + 2, col, 2)
        for dc in range(-2, 3):
            put(out, r - 2, c + dc, 5)
            put(out, r + 2, c + dc, 8)
        put(out, r - 1, c, 5)
        for dr in (-1, 0, 1):
            put(out, r + dr, c - 2, 2)
            put(out, r + dr, c + 2, 2)
    return out
