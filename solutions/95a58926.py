def solve(grid):
    h, w = len(grid), len(grid[0])
    vals = {v for row in grid for v in row if v not in (0, 5)}
    if len(vals) != 1:
        return [r[:] for r in grid]
    marker = next(iter(vals))
    rows = [r for r in range(h) if grid[r].count(5) > w // 2]
    cols = [c for c in range(w) if sum(grid[r][c] == 5 for r in range(h)) > h // 2]
    if not rows or not cols:
        return [r[:] for r in grid]
    out = [[0] * w for _ in range(h)]
    for r in rows:
        for c in range(w):
            out[r][c] = 5
    for c in cols:
        for r in range(h):
            out[r][c] = 5
    for r in rows:
        for c in cols:
            out[r][c] = marker
    return out
