def solve(grid):
    h, w = len(grid), len(grid[0])
    cand = []
    for s in {v for r in grid for v in r if v}:
        rows = [r for r in range(h) if all(v == s for v in grid[r])]
        cols = [c for c in range(w) if all(grid[r][c] == s for r in range(h))]
        if rows and cols:
            cand.append((s, rows, cols))
    if len(cand) != 1:
        return [r[:] for r in grid]
    s, rows, cols = cand[0]
    rs = [0] + [r + 1 for r in rows]
    re = rows + [h]
    cs = [0] + [c + 1 for c in cols]
    ce = cols + [w]
    out = []
    for t, b in zip(rs, re):
        line = []
        for l, r in zip(cs, ce):
            vals = {grid[i][j] for i in range(t, b) for j in range(l, r) if grid[i][j] != s}
            if len(vals) > 1:
                return [r[:] for r in grid]
            line.append(next(iter(vals), 0))
        out.append(line[::-1])
    return out
