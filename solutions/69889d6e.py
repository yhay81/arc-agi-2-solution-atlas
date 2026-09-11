def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = cp(g)
    r, c = points(g, 2)[0]
    h, w = (len(g), len(g[0]))
    for _ in range(h * w):
        if r <= 0 or c >= w:
            break
        if g[r - 1][c] == 1:
            c += 1
            if c < w:
                out[r][c] = 2
            continue
        r -= 1
        out[r][c] = 2
        c += 1
        if c < w:
            out[r][c] = 2
    return out
