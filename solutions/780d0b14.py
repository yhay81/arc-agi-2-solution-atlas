def solve(grid):
    h, w = len(grid), len(grid[0])
    rs = [r for r in range(h) if all(v == 0 for v in grid[r])]
    cs = [c for c in range(w) if all(grid[r][c] == 0 for r in range(h))]
    if not rs or not cs:
        return [r[:] for r in grid]
    re = [-1] + rs + [h]
    ce = [-1] + cs + [w]
    rr = [(a + 1, b) for a, b in zip(re, re[1:]) if b > a + 1]
    cr = [(a + 1, b) for a, b in zip(ce, ce[1:]) if b > a + 1]
    if len(rr) < 2 or len(cr) < 2:
        return [r[:] for r in grid]
    out = []
    for a, b in rr:
        line = []
        for c, d in cr:
            vals = {grid[r][j] for r in range(a, b) for j in range(c, d) if grid[r][j]}
            if len(vals) != 1:
                return [r[:] for r in grid]
            line.append(next(iter(vals)))
        out.append(line)
    return out
