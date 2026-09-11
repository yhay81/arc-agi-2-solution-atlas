def empty(g, color=0):
    return [[color] * len(g[0]) for _ in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    r, c = (h // 2, w // 2)
    color = g[r][c]
    quadrants = {int(a > r) * 2 + int(b > c) for a, b in points(g, color) if a != r and b != c}
    if len(quadrants) != 1:
        raise ValueError("Ambiguous quadrant")
    q = quadrants.pop()
    dr = 1 if q // 2 else -1
    dc = 1 if q % 2 else -1
    out = empty(g, 7)
    while 0 <= r < h and 0 <= c < w:
        out[r][c] = color
        r += dr
        c += dc
    return out
