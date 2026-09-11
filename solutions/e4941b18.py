def solve(grid):
    a = grid
    out = [row[:] for row in a]
    r, c = next(((r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == 8))
    rr, rc = next(((r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == 2))
    pts = [(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == 5]
    l = min((c for r, c in pts))
    right = max((c for r, c in pts))
    dest = l - 1 if rc > c else right + 1
    out[rr][rc] = 7
    out[r][c] = 2
    out[-1][dest] = 8
    return out
