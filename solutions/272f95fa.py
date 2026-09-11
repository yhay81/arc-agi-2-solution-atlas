def solve(grid):
    h, w = len(grid), len(grid[0])
    sr = [r for r in range(h) if len(set(grid[r])) == 1 and grid[r][0] != 0]
    sc = [c for c in range(w) if len({grid[r][c] for r in range(h)}) == 1 and grid[0][c] != 0]
    if not sr or not sc:
        return [r[:] for r in grid]
    re = [-1] + sr + [h]
    ce = [-1] + sc + [w]
    pal = [[0, 2, 0], [4, 6, 3], [0, 1, 0]]
    out = [r[:] for r in grid]
    for i, (t, b) in enumerate(zip(re, re[1:])):
        for j, (l, r) in enumerate(zip(ce, ce[1:])):
            if b <= t + 1 or r <= l + 1 or i >= len(pal) or j >= len(pal[i]) or not pal[i][j]:
                continue
            for x in range(t + 1, b):
                out[x][l + 1 : r] = [pal[i][j]] * (r - l - 1)
    return out
