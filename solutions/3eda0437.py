def solve(grid):
    h, w = len(grid), len(grid[0])
    cand = []
    for top in range(h - 1):
        valid = [True] * w
        for bottom in range(top, h):
            valid = [x and grid[bottom][c] == 0 for c, x in enumerate(valid)]
            if bottom == top:
                continue
            start = None
            for c in range(w + 1):
                if c < w and valid[c]:
                    if start is None:
                        start = c
                elif start is not None:
                    if c - start >= 2:
                        cand.append(((bottom - top + 1) * (c - start), top, bottom, start, c - 1))
                    start = None
    if not cand:
        return [r[:] for r in grid]
    m = max(x[0] for x in cand)
    best = [x for x in cand if x[0] == m]
    if len(best) != 1:
        return [r[:] for r in grid]
    _, t, b, l, r = best[0]
    out = [row[:] for row in grid]
    for i in range(t, b + 1):
        out[i][l : r + 1] = [6] * (r - l + 1)
    return out
