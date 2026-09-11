def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    out = cp(g)
    for r, row in enumerate(g):
        for pair in ({1, 8}, {4, 7}):
            ps = [c for c, v in enumerate(row) if v in pair]
            if len(ps) == 2 and {row[c] for c in ps} == pair:
                a, b = ps
                out[r][b] = 0
                out[r][a + 1] = row[b]
    return out
