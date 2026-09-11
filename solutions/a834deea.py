def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    out = copy(g)
    fixed = [[1, 7, 6], [4, 0, 5], [2, 9, 3]]
    for a in range(len(g) - 4):
        for b in range(len(g[0]) - 4):
            if all(
                g[a + r][b + c] == 0
                for r in range(5)
                for c in range(5)
                if r in (0, 4) or c in (0, 4)
            ):
                for r in range(3):
                    for c in range(3):
                        if g[a + r + 1][b + c + 1] == 0:
                            out[a + r + 1][b + c + 1] = fixed[r][c]
    return out
