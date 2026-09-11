def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    return [
        [g[r % h][c % w] if g[r // h][c // w] == 5 else 0 for c in range(w * w)]
        for r in range(h * h)
    ]
