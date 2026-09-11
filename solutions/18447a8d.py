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
    bg = 7
    n = (len(a[0]) - 1) // 2
    out = [[bg] * len(a[0]) for row in a]
    pieces = []
    for v, pts in cc(a, bg):
        if v == 8:
            for r, c in pts:
                out[r][c] = v
        else:
            r0 = min((r for r, c in pts))
            c0 = min((c for r, c in pts))
            pieces.append((v, {(r - r0, c - c0) for r, c in pts}))
    used = set()
    for r0 in range(1, len(a) - 1, 4):
        missing = {(r, c) for r in range(3) for c in range(n) if a[r0 + r][c] == bg}
        mr = min((r for r, c in missing))
        mc = min((c for r, c in missing))
        norm = {(r - mr, c - mc) for r, c in missing}
        matches = [j for j, (v, pts) in enumerate(pieces) if j not in used and pts == norm]
        if not (len(matches) == 1):
            raise ValueError("task assumptions are not satisfied")
        j = matches[0]
        used.add(j)
        v = pieces[j][0]
        for r, c in missing:
            out[r0 + r][c] = v
    return out
