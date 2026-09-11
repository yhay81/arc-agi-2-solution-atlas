def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    out = cp(g)
    for a in range(h - 3):
        for b in range(a + 3, h):
            cols = [all(g[r][c] == 0 for r in range(a, b + 1)) for c in range(w)]
            for c in range(w - 3):
                for d in range(c + 3, w):
                    if all(cols[c : d + 1]):
                        for r in range(a + 1, b):
                            for col in range(c + 1, d):
                                out[r][col] = 8
    return out
