def solve(grid):
    h, w = len(grid), len(grid[0])
    pos = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v]
    if len(pos) != 3 or len({grid[r][c] for r, c in pos}) != 1:
        return [row[:] for row in grid]
    pos.sort()
    rs = pos[1][0] - pos[0][0]
    cs = pos[1][1] - pos[0][1]
    if not rs or abs(rs) != abs(cs) or pos[2][0] - pos[1][0] != rs or pos[2][1] - pos[1][1] != cs:
        return [row[:] for row in grid]
    cr, cc = pos[1]
    step = abs(rs)
    color = grid[pos[0][0]][pos[0][1]]
    out = [[0] * w for _ in range(h)]
    radius = 0
    while radius <= max(cr, cc, h - 1 - cr, w - 1 - cc):
        for r in range(cr - radius, cr + radius + 1):
            for c in range(cc - radius, cc + radius + 1):
                if 0 <= r < h and 0 <= c < w and max(abs(r - cr), abs(c - cc)) == radius:
                    out[r][c] = color
        radius += step
    return out
