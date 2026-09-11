def solve(grid):
    g = grid
    h, w = len(g), len(g[0])
    colors = {v for row in g for v in row if v}
    frames = []
    for v in colors:
        p = [(r, c) for r in range(h) for c in range(w) if g[r][c] == v]
        a, b = min(r for r, _ in p), max(r for r, _ in p)
        c, d = min(c for _, c in p), max(c for _, c in p)
        inside = {(r, z) for r in range(a + 1, b) for z in range(c + 1, d) if g[r][z] == v}
        frames.append((v, a, b, c, d, inside))
    v, a, b, c, d, p = max(frames, key=lambda t: len(t[-1]))
    out = [[0] * w for _ in range(h)]
    for color, x, y, z, t, _ in frames:
        if (y - x, t - z) != (b - a, d - c):
            continue
        for r in range(x, y + 1):
            for col in range(z, t + 1):
                if r in (x, y) or col in (z, t):
                    out[r][col] = color
        for r, col in p:
            rr, cc = r + x - a, col + z - c
            if 0 <= rr < h and 0 <= cc < w:
                out[rr][cc] = color
    return out
