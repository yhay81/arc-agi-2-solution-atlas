def solve(grid):
    h, w = len(grid), len(grid[0])
    rows = [r for r in range(h) if sum(v != 0 for v in grid[r]) >= 2]
    cols = [c for c in range(w) if sum(grid[r][c] != 0 for r in range(h)) >= 2]
    if len(rows) != 1 or len(cols) != 1:
        return [r[:] for r in grid]
    cr, cc = rows[0], cols[0]
    hp = [c for c, v in enumerate(grid[cr]) if v]
    vp = [r for r in range(h) if grid[r][cc]]
    l, r = min(hp), max(hp)
    t, b = min(vp), max(vp)
    horizontal = grid[cr][l : r + 1]
    vertical = [grid[x][cc] for x in range(t, b + 1)]
    if (
        0 in horizontal
        or 0 in vertical
        or sum(v != 0 for row in grid for v in row) != len(horizontal) + len(vertical) - 1
    ):
        return [x[:] for x in grid]
    out = [x[:] for x in grid]
    for c in range(w):
        out[cr][c] = horizontal[(c - l) % len(horizontal)]
    for x in range(h):
        v = vertical[(x - t) % len(vertical)]
        if x == cr and out[x][cc] != v:
            return [z[:] for z in grid]
        out[x][cc] = v
    return out
