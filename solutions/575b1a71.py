def cp(g):
    return [list(r) for r in g]


def solve(grid):
    g = grid
    cols = [c for c in range(len(g[0])) if any(row[c] == 0 for row in g)]
    o = cp(g)
    for i, c in enumerate(cols):
        for r in range(len(g)):
            if g[r][c] == 0:
                o[r][c] = i % 4 + 1
    return o
