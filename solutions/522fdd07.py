def cc(a, bg=0, colorwise=True):
    h, w = (len(a), len(a[0]))
    seen = set()
    out = []
    for r in range(h):
        for c in range(w):
            if a[r][c] == bg or (r, c) in seen:
                continue
            color = a[r][c]
            q = [(r, c)]
            seen.add((r, c))
            cells = []
            for rr, cc_ in q:
                cells.append((rr, cc_))
                for nr, nc in [(rr - 1, cc_), (rr + 1, cc_), (rr, cc_ - 1), (rr, cc_ + 1)]:
                    if (
                        0 <= nr < h
                        and 0 <= nc < w
                        and ((nr, nc) not in seen)
                        and (a[nr][nc] != bg)
                        and (not colorwise or a[nr][nc] == color)
                    ):
                        seen.add((nr, nc))
                        q.append((nr, nc))
            out.append((color, cells))
    return out


def solve(grid):
    a = grid
    bg = 7
    out = [[bg] * len(a[0]) for row in a]
    for v, pts in cc(a, bg):
        r0 = min((r for r, c in pts))
        r1 = max((r for r, c in pts))
        c0 = min((c for r, c in pts))
        c1 = max((c for r, c in pts))
        n = r1 - r0 + 1
        if not (n == c1 - c0 + 1):
            raise ValueError("task assumptions are not satisfied")
        m = n - 2 if n > 1 else 9
        cr = (r0 + r1) // 2
        cc_ = (c0 + c1) // 2
        for r in range(cr - m // 2, cr + m // 2 + 1):
            for c in range(cc_ - m // 2, cc_ + m // 2 + 1):
                if 0 <= r < len(a) and 0 <= c < len(a[0]):
                    out[r][c] = v
    return out
