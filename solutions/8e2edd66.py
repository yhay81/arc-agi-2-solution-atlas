def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    color = next(v for row in g for v in row if v)
    inverse = [[color if v == 0 else 0 for v in row] for row in g]
    out = [[0] * (w * w) for _ in range(h * h)]
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            if v == 0:
                for a in range(h):
                    for b in range(w):
                        out[r * h + a][c * w + b] = inverse[a][b]
    return out
