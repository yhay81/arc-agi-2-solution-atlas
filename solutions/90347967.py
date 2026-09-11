def solve(grid):
    g = grid
    a, b = next(((r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 5))
    out = [[0] * len(g[0]) for _ in g]
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            if v:
                x, y = (2 * a - r, 2 * b - c)
                if not (0 <= x < len(g) and 0 <= y < len(g[0])):
                    raise ValueError("Rotation leaves the canvas")
                out[x][y] = v
    return out
