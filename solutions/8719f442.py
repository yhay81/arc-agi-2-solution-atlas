def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    out = [[0] * (w * (w + 2)) for _ in range(h * (h + 2))]
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            for a in range(h):
                for b in range(w):
                    out[h + r * h + a][w + c * w + b] = v
            if not v:
                continue
            destinations = []
            if r == 0:
                destinations.append((0, c + 1))
            if r == h - 1:
                destinations.append((h + 1, c + 1))
            if c == 0:
                destinations.append((r + 1, 0))
            if c == w - 1:
                destinations.append((r + 1, w + 1))
            for mr, mc in destinations:
                for a in range(h):
                    for b in range(w):
                        out[mr * h + a][mc * w + b] = g[a][b]
    return out
