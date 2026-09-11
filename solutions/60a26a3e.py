def solve(grid):
    h, w = len(grid), len(grid[0])
    centers = []
    for r in range(1, h - 1):
        for c in range(1, w - 1):
            if grid[r][c] == 0 and all(
                grid[r + dr][c + dc] == 2 for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))
            ):
                centers.append((r, c))
    if len(centers) < 2:
        return [r[:] for r in grid]
    out = [r[:] for r in grid]
    for r in {r for r, _ in centers}:
        cs = sorted(c for rr, c in centers if rr == r)
        for l, q in zip(cs, cs[1:]):
            for c in range(l + 2, q - 1):
                out[r][c] = 1
    for c in {c for _, c in centers}:
        rs = sorted(r for r, cc in centers if cc == c)
        for t, b in zip(rs, rs[1:]):
            for r in range(t + 2, b - 1):
                out[r][c] = 1
    return out
