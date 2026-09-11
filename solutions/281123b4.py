def solve(grid):
    g = grid
    order = (5, 8, 4, 9)
    g = [row[:] for row in g]
    h = len(g)
    w = (len(g[0]) - 3) // 4
    out = [[0] * w for _ in range(h)]
    panels = {
        next(v for row in g for v in row[i * (w + 1) : i * (w + 1) + w] if v): [
            row[i * (w + 1) : i * (w + 1) + w] for row in g
        ]
        for i in range(4)
    }
    for color in order:
        for r in range(h):
            for c in range(w):
                if panels[color][r][c]:
                    out[r][c] = color
    return out
