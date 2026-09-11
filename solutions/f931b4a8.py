def solve(grid):
    a = grid
    a = [row[:] for row in a]
    h, w = len(a), len(a[0])
    hh, ww = (h // 2, w // 2)
    n = sum(v != 0 for row in a[:hh] for v in row[:ww])
    m = sum(v != 0 for row in a[:hh] for v in row[ww:])
    base = [row[:ww] for row in a[hh:]]
    tile = [row[ww:] for row in a[hh:]]
    out = [[0] * m for _ in range(n)]
    if not any(v for row in tile for v in row):
        return [[base[r % hh][c % ww] for c in range(m)] for r in range(n)]
    for r in range(n):
        for c in range(m):
            v = tile[r % hh][c % ww]
            out[r][c] = v if v else base[(r // hh) % hh][(c // ww) % ww]
    return out
