def solve(grid):
    g = grid
    mapping = {g[r][c]: g[r][1 - c] for r in range(2) for c in range(2)}
    return [
        [v if r < 2 and c < 2 else mapping.get(v, v) for c, v in enumerate(row)]
        for r, row in enumerate(g)
    ]
