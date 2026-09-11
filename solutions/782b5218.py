def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = cp(g)
    fill = (set(v for row in g for v in row) - {0, 2}).pop()
    out = cp(g)
    for c in range(len(g[0])):
        rs = [r for r, row in enumerate(g) if row[c] == 2]
        if not rs:
            for r in range(len(g)):
                out[r][c] = 0
            continue
        for r in range(len(g)):
            if g[r][c] != 2:
                out[r][c] = 0 if r < min(rs) else fill
    return out
