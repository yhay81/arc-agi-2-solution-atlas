def solve(grid):
    g = grid
    color = g[0][0]
    h, w = (len(g), len(g[0]))
    return [
        [color if (r + 1) % (h + 1) == 0 or (c + 1) % (w + 1) == 0 else 0 for c in range(15)]
        for r in range(15)
    ]
