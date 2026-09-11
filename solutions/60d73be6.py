def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    h, w = (len(g), len(g[0]))
    r0 = next((r for r, row in enumerate(g) if len(set(row)) == 1 and row[0] != 7))
    color = g[r0][0]
    c0 = next(c for c in range(w) if all(row[c] == color for row in g))
    out = copy(g)
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            if v in (7, color):
                continue
            for a in (r, 2 * r0 - r):
                for b in (c, 2 * c0 - c):
                    if 0 <= a < h and 0 <= b < w:
                        out[a][b] = v
    return out
