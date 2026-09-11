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
    a = [row[:] for row in a]
    out = [row[:] for row in a]
    for v, pts in cc(a, 7):
        n = len(pts)
        h = max((r for r, c in pts)) - min((r for r, c in pts)) + 1
        w = max((c for r, c in pts)) - min((c for r, c in pts)) + 1
        color = 2 if n == 3 and min(h, w) == 1 else 4 if n == 3 else {2: 9, 4: 8, 5: 3, 6: 5}[n]
        for r, c in pts:
            out[r][c] = color
    return out
