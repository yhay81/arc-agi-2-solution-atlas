def solve(grid):
    h, w = len(grid), len(grid[0])
    if h < 3 or w < 3:
        return [r[:] for r in grid]
    sr = [r for r in range(h) if len(set(grid[r])) == 1 and grid[r][0]]
    sc = [c for c in range(w) if len({grid[r][c] for r in range(h)}) == 1 and grid[0][c]]
    if len(sr) != 2 or len(sc) != 2 or grid[sr[0]][0] != grid[0][sc[0]]:
        return [r[:] for r in grid]
    top, bottom = sr[0] + 1, sr[1]
    left, right = sc[0] + 1, sc[1]
    if top >= bottom or left >= right:
        return [r[:] for r in grid]
    corners = [grid[0][0], grid[0][-1], grid[-1][0], grid[-1][-1]]
    if 0 in corners or len(set(corners)) != 4:
        return [r[:] for r in grid]
    ch, cw = bottom - top, right - left
    rm, cm = ch // 2, cw // 2
    out = [grid[r][left:right] for r in range(top, bottom)]
    for r in range(ch):
        for c in range(cw):
            if out[r][c]:
                out[r][c] = corners[(0 if r < rm else 1) * 2 + (0 if c < cm else 1)]
    return out
