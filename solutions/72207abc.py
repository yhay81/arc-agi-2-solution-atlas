def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = cp(g)
    out = cp(g)
    for r, row in enumerate(g):
        marks = [(c, v) for c, v in enumerate(row) if v != 0]
        if not marks:
            continue
        cs = [v for c, v in marks]
        c = marks[0][0]
        n = 0
        out[r] = [0] * len(row)
        while c < len(row):
            out[r][c] = cs[n % len(cs)]
            n += 1
            c += n
    return out
