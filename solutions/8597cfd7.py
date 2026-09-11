def solve(grid):
    g = grid
    divider = next(r for r, row in enumerate(g) if set(row) == {5})
    delta = {
        color: sum(v == color for row in g[divider + 1 :] for v in row)
        - sum(v == color for row in g[:divider] for v in row)
        for color in (2, 4)
    }
    chosen = max(delta, key=delta.get)
    return [[chosen] * 2 for _ in range(2)]
