def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    colors = {v for row in a for v in row if v}
    cand = []
    for color in colors:
        ps = [(r, c) for r in range(h) for c in range(w) if a[r][c] == color]
        t, l = min(r for r, c in ps), min(c for r, c in ps)
        b, r = max(x for x, c in ps), max(c for x, c in ps)
        if all(a[y][x] == color for y in range(t, b + 1) for x in range(l, r + 1)) and (
            (t == 0 and b == h - 1) or (l == 0 and r == w - 1)
        ):
            cand.append((color, t, b, l, r))
    if len(cand) != 1 or len(colors) < 2:
        return [row[:] for row in a]
    color, t, b, l, r = cand[0]
    out = [[0] * w for _ in range(h)]
    for y in range(t, b + 1):
        for x in range(l, r + 1):
            out[y][x] = color
    if t == 0 and b == h - 1:
        for y in range(h):
            lc = sum(v != 0 and v != color for v in a[y][:l])
            rc = sum(v != 0 and v != color for v in a[y][r + 1 :])
            for x in range(max(0, l - lc), l):
                out[y][x] = color
            for x in range(r + 1, min(w, r + 1 + rc)):
                out[y][x] = color
    else:
        for x in range(w):
            tc = sum(a[y][x] != 0 and a[y][x] != color for y in range(t))
            bc = sum(a[y][x] != 0 and a[y][x] != color for y in range(b + 1, h))
            for y in range(max(0, t - tc), t):
                out[y][x] = color
            for y in range(b + 1, min(h, b + 1 + bc)):
                out[y][x] = color
    return out
