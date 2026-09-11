def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    out = copy(g)
    for top in range(0, len(g), 10):
        for left in range(0, len(g[0]), 10):
            values = [[g[top + r][left + c] for c in (2, 6)] for r in (2, 6)]
            if g[top][left + 4] == 4:
                values = [row[::-1] for row in values]
            elif g[top + 4][left] == 4:
                values = values[::-1]
            else:
                colors = {v for row in values for v in row if v != 1}
                if len(colors) != 1:
                    raise ValueError("color to copy is not unique")
                color = next(iter(colors))
                values = [[color] * 2 for _ in range(2)]
            for i in range(2):
                for j in range(2):
                    for r in range(top + 1 + 4 * i, top + 4 + 4 * i):
                        for c in range(left + 1 + 4 * j, left + 4 + 4 * j):
                            out[r][c] = values[i][j]
    return out
