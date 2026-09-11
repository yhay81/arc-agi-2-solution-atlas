def solve(grid):
    g = grid
    return [
        [
            0 if r % 2 and c % 2 and r < len(g) - 1 and c < len(g[0]) - 1 else 1
            for c in range(len(g[0]))
        ]
        for r in range(len(g))
    ]
