def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    op = [(r, c) for r in range(h) for c in range(w) if a[r][c] == 3]
    mk = [(r, c) for r in range(h) for c in range(w) if a[r][c] == 6]
    if not op or not mk:
        return [r[:] for r in a]
    t, l = min(r for r, c in op), min(c for r, c in op)
    b, r = max(r for r, c in op), max(c for r, c in op)
    nt, nl, nb, nr = t, l, b, r
    for y, x in mk:
        if y < t:
            nt = min(nt, y + 1)
        elif y > b:
            nb = max(nb, y - 1)
        if x < l:
            nl = min(nl, x + 1)
        elif x > r:
            nr = max(nr, x - 1)
    out = [row[:] for row in a]
    for y, x in (
        [(y, l) for y in range(t, b + 1)]
        + [(y, r) for y in range(t, b + 1)]
        + [(t, x) for x in range(l, r + 1)]
        + [(b, x) for x in range(l, r + 1)]
    ):
        if (
            (x == l and nl != l)
            or (x == r and nr != r)
            or (y == t and nt != t)
            or (y == b and nb != b)
        ):
            out[y][x] = 0
    for x in range(l + 1, r):
        if all(a[y][x] == 3 for y in range(t, b + 1)):
            for y in range(nt, nb + 1):
                out[y][x] = 3
    for y in range(t + 1, b):
        if all(a[y][x] == 3 for x in range(l, r + 1)):
            for x in range(nl, nr + 1):
                out[y][x] = 3
    for x in range(nl, nr + 1):
        out[nt][x] = out[nb][x] = 3
    for y in range(nt, nb + 1):
        out[y][nl] = out[y][nr] = 3
    return out
