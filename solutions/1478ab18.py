def solve(grid):
    a = grid
    a = [row[:] for row in a]
    pts = [(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == 5]
    r0 = min((r for r, c in pts))
    r1 = max((r for r, c in pts))
    c0 = min((c for r, c in pts))
    c1 = max((c for r, c in pts))
    corners = {(r0, c0), (r0, c1), (r1, c0), (r1, c1)}
    missing = corners - set(pts)
    if not (len(missing) == 1):
        raise ValueError("task assumptions are not satisfied")
    mr, mc = missing.pop()
    out = [row[:] for row in a]
    for c in range(c0, c1 + 1):
        out[mr][c] = 8
    for r in range(r0, r1 + 1):
        out[r][mc] = 8
    ends = [p for p in corners if p != (mr, mc) and (p[0] == mr or p[1] == mc)]
    (ar, ac), (br, bc) = ends
    n = max(abs(ar - br), abs(ac - bc))
    for i in range(n + 1):
        out[ar + (br - ar) * i // n][ac + (bc - ac) * i // n] = 8
    for r, c in pts:
        out[r][c] = 5
    return out
