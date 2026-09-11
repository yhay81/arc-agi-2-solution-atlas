def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    out = copy(g)
    for c, v in enumerate(g[-1]):
        if not v:
            continue
        color = v
        for r in range(len(g) - 1, -1, -1):
            if c and c + 1 < len(g[0]) and g[r][c - 1] and (g[r][c - 1] == g[r][c + 1]):
                color = g[r][c - 1]
            out[r][c] = color
    return out
