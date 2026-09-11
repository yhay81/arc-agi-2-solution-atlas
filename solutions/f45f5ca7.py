def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    out = cp(g)
    for r, row in enumerate(g):
        if row[0] != 0:
            out[r][0] = 0
            out[r][{8: 1, 2: 2, 4: 3, 3: 4}[row[0]]] = row[0]
    return out
