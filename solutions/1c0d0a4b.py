def cp(g):
    return [list(r) for r in g]


def solve(grid):
    g = grid
    o = cp(g)
    for r in range(1, len(g), 4):
        for c in range(1, len(g[0]), 4):
            for i in range(r, min(r + 3, len(g))):
                for j in range(c, min(c + 3, len(g[0]))):
                    o[i][j] = 2 if g[i][j] == 0 else 0
    return o
