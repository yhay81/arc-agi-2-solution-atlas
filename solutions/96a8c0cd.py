def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    h, w = (len(g), len(g[0]))
    out = copy(g)
    r, c = next(((r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 2))
    dr, dc = (1, 0) if r == 0 else (-1, 0) if r == h - 1 else (0, 1) if c == 0 else (0, -1)
    seen = set()
    while True:
        if (r, c) in seen:
            raise ValueError("path forms a cycle")
        seen.add((r, c))
        out[r][c] = 2
        a, b = (r + dr, c + dc)
        if not (0 <= a < h and 0 <= b < w):
            break
        if g[a][b] in (1, 3):
            vr, vc = (-dc, dr) if g[a][b] == 1 else (dc, -dr)
            while 0 <= a < h and 0 <= b < w and (g[a][b] in (1, 3)):
                r += vr
                c += vc
                if not (0 <= r < h and 0 <= c < w):
                    raise ValueError("avoidance direction leaves the grid")
                out[r][c] = 2
                a, b = (r + dr, c + dc)
        r, c = (a, b)
    return out
