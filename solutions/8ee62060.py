from itertools import product


def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    o = [[0] * w for _ in g]
    for r in range(0, h, 2):
        for c in range(0, w, 2):
            for i, j in product(range(2), repeat=2):
                o[r + i][w - c - 2 + j] = g[r + i][c + j]
    return o
