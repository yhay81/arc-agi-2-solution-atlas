from collections import Counter


def cp(g):
    return [row[:] for row in g]


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    out = cp(g)
    axis = next((r for r, row in enumerate(g) if all(v == 9 for v in row)))
    background = bg(g)
    dest = []
    for r, c in points(g, 2):
        directions = [
            (dr, dc)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
            if 0 <= r + dr < h and 0 <= c + dc < w and (g[r + dr][c + dc] == 6)
        ]
        if len(directions) != 1:
            raise ValueError("Motion direction ambiguous")
        dr, dc = directions[0]
        while 0 <= r + dr < h and 0 <= c + dc < w and (g[r + dr][c + dc] == 6):
            r += dr
            c += dc
        dest.append((r, c))
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            if v in (2, 5, 6):
                out[r][c] = background
    for r, c in dest:
        out[r][c] = 2
        put(out, 2 * axis - r, c, 5)
    return out
