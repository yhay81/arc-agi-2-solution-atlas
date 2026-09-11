def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    out = copy(g)
    used = set()
    for size in range(min(len(g), len(g[0])), 1, -1):
        for r in range(len(g) - size + 1):
            for c in range(len(g[0]) - size + 1):
                cells = {(a, b) for a in range(r, r + size) for b in range(c, c + size)}
                if not cells & used and all((g[a][b] == 0 for a, b in cells)):
                    used |= cells
                    for a, b in cells:
                        out[a][b] = 1
    return out
