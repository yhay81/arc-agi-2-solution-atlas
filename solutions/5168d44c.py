def solve(grid):
    h, w = len(grid), len(grid[0])
    pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    if not pts:
        return [r[:] for r in grid]
    t, l = min(r for r, _ in pts), min(c for _, c in pts)
    b, q = max(r for r, _ in pts), max(c for _, c in pts)
    if (b - t, q - l) != (2, 2):
        return [r[:] for r in grid]
    if (
        any(grid[t][c] != 2 or grid[b][c] != 2 for c in range(l, q + 1))
        or any(grid[r][l] != 2 or grid[r][q] != 2 for r in range(t, b + 1))
        or grid[t + 1][l + 1] != 3
    ):
        return [r[:] for r in grid]
    guide = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 3]
    if len({c for _, c in guide}) == 1:
        dr, dc = 2, 0
    elif len({r for r, _ in guide}) == 1:
        dr, dc = 0, 2
    else:
        return [r[:] for r in grid]
    nt, nl = t + dr, l + dc
    if nt + 3 > h or nl + 3 > w:
        return [r[:] for r in grid]
    out = [r[:] for r in grid]
    for r in range(t, b + 1):
        for c in range(l, q + 1):
            out[r][c] = 0
    out[t + 1][l + 1] = 3
    for r in range(nt, nt + 3):
        for c in range(nl, nl + 3):
            out[r][c] = 3 if (r, c) == (nt + 1, nl + 1) else 2
    return out
