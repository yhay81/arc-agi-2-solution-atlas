def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    out = [row[:] for row in g]
    for r in range(h):
        for c in range(w):
            if g[r][c] != 8:
                continue
            for gap in range(1, min(r, c, h - 1 - r, w - 1 - c)):
                points = [
                    (r + dr * k, c + dc * k)
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for k in (gap, gap + 1)
                ]
                if all((g[a][b] == 1 for a, b in points)):
                    out[r][c] = 4
                    break
    return out
