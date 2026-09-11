def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    ps = [(r, c) for r in range(h) for c in range(w) if a[r][c]]
    if len(ps) != 2:
        return [r[:] for r in a]
    (ra, ca), (rb, cb) = ps
    x, y = a[ra][ca], a[rb][cb]
    out = [r[:] for r in a]
    if ra == rb and ca != cb:
        if ca > cb:
            ra, ca, rb, cb = rb, cb, ra, ca
            x, y = y, x
        l = (ca + cb - 3) // 2
        r = l + 3
        for rr in range(ra - 2, ra + 3):
            if 0 <= rr < h:
                out[rr][l] = x
                out[rr][r] = y
                if rr in (ra - 2, ra + 2):
                    out[rr][l + 1] = x
                    out[rr][r - 1] = y
        for c in range(ca, l):
            out[ra][c] = x
        for c in range(r + 1, cb + 1):
            out[ra][c] = y
    elif ca == cb and ra != rb:
        if ra > rb:
            ra, ca, rb, cb = rb, cb, ra, ca
            x, y = y, x
        t = (ra + rb - 3) // 2
        b = t + 3
        for cc in range(ca - 2, ca + 3):
            if 0 <= cc < w:
                out[t][cc] = x
                out[b][cc] = y
                if cc in (ca - 2, ca + 2):
                    out[t + 1][cc] = x
                    out[b - 1][cc] = y
        for r in range(ra, t):
            out[r][ca] = x
        for r in range(b + 1, rb + 1):
            out[r][ca] = y
    return out
