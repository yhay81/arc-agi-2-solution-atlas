def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    out = [[0 if v == 4 else v for v in row] for row in g]
    line = next((r for r, row in enumerate(g) if all(v == 2 for v in row)))
    for r, c in points(g, 4):
        rr = r + 1
        put(out, rr, c, 4)
        if rr == line - 1:
            for dc in (-1, 1):
                x, y = (rr - 1, c + dc)
                while 0 <= x < h and 0 <= y < w:
                    out[x][y] = 4
                    x -= 1
                    y += dc
    return out
