def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    bg = max({v for row in a for v in row}, key=lambda v: sum(x == v for row in a for x in row))
    blocks = []
    covered = set()
    for r in range(h - 4):
        for c in range(w - 4):
            co = a[r][c]
            if (
                co != bg
                and all(a[rr][cc] == co for rr in range(r, r + 5) for cc in range(c, c + 5))
                and (r == 0 or a[r - 1][c] != co)
                and (c == 0 or a[r][c - 1] != co)
            ):
                blocks.append((r, c, co))
                covered |= {(rr, cc) for rr in range(r, r + 5) for cc in range(c, c + 5)}
    ys = sorted({r for r, c, v in blocks})
    xs = sorted({c for r, c, v in blocks})
    if not (len(blocks) == len(ys) * len(xs)):
        raise ValueError("task assumptions are not satisfied")
    out = [[bg] * (6 * len(xs) + 1) for _ in range(6 * len(ys) + 1)]
    for r, c, co in blocks:
        pts = [
            (rr, cc)
            for rr in range(h)
            for cc in range(w)
            if a[rr][cc] == co and (rr, cc) not in covered
        ]
        y, x = min(rr for rr, cc in pts), min(cc for rr, cc in pts)
        i, j = ys.index(r), xs.index(c)
        for rr in range(1 + 6 * i, 6 + 6 * i):
            for cc in range(1 + 6 * j, 6 + 6 * j):
                out[rr][cc] = co
        for rr in range(3):
            for cc in range(3):
                if a[y + rr][x + cc] == co:
                    out[2 + 6 * i + rr][2 + 6 * j + cc] = bg
    return out
