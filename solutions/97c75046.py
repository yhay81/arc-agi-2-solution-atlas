def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    out = copy(g)
    h, w = (len(g), len(g[0]))
    r, c = next(((r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 5))
    out[r][c] = 7
    hits = []
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        k = 1
        while 0 <= r + k * dr < h and 0 <= c + k * dc < w:
            if g[r + k * dr][c + k * dc] == 0:
                hits.append((k, dr, dc))
                break
            k += 1
    k, dr, dc = min(hits)
    r += (k - 1) * dr
    c += (k - 1) * dc
    sides = [
        (vr, vc)
        for vr, vc in ((-dc, dr), (dc, -dr))
        if 0 <= r + dr + vr < h and 0 <= c + dc + vc < w and (g[r + dr + vr][c + dc + vc] == 7)
    ]
    if len(sides) == 1:
        vr, vc = sides[0]
        while 0 <= r + dr < h and 0 <= c + dc < w and (g[r + dr][c + dc] == 0):
            a, b = (r + dr + vr, c + dc + vc)
            if not (0 <= a < h and 0 <= b < w) or g[a][b] != 7:
                break
            r, c = (a, b)
    out[r][c] = 5
    return out
