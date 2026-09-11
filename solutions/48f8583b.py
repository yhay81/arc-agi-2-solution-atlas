from collections import Counter


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    counts = Counter(v for row in g for v in row)
    color = min(counts, key=counts.get)
    out = [[0] * (w * w) for _ in range(h * h)]
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            if v == color:
                for a in range(h):
                    for b in range(w):
                        out[r * h + a][c * w + b] = g[a][b]
    return out
