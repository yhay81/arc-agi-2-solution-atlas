def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    out = [row[:] for row in g]
    starts = [c for c in range(1, w - 1) if g[0][c] == 0 and g[0][c - 1] == g[0][c + 1] == 7]
    if len(starts) != 1:
        raise ValueError("Expected one top entrance")
    r, c = (0, starts[0])
    dr, dc = (1, 0)
    seen = set()
    while True:
        if (r, c, dr, dc) in seen:
            raise ValueError("Corridor loop")
        seen.add((r, c, dr, dc))
        a, b = (r + dr, c + dc)
        blocked = 0 <= a < h and 0 <= b < w and (g[a][b] == 7)
        if g[r][c] == 9 and blocked:
            break
        out[r][c] = 8
        if not (0 <= a < h and 0 <= b < w):
            break
        if blocked:
            options = [
                (x, y)
                for x, y in [(-dc, dr), (dc, -dr)]
                if 0 <= r + x < h and 0 <= c + y < w and (g[r + x][c + y] != 7)
            ]
            if len(options) != 1:
                raise ValueError("Corridor branch")
            dr, dc = options[0]
            a, b = (r + dr, c + dc)
        r, c = (a, b)
    return out
