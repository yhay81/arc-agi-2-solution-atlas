def bounds(points):
    return (
        min(r for r, c in points),
        min(c for r, c in points),
        max(r for r, c in points),
        max(c for r, c in points),
    )


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    ps = [(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v]
    r, c, b, d = bounds(ps)
    outer = a[r][c]
    core = [(y, x) for y, row in enumerate(a) for x, v in enumerate(row) if v and v != outer]
    y, x, z, w = bounds(core)
    color = a[core[0][0]][core[0][1]]
    pad = min(z - y + 1, w - x + 1, r, c, len(a) - 1 - b, len(a[0]) - 1 - d)
    out = [row[:] for row in a]
    for yy in range(r - pad, b + pad + 1):
        for xx in range(c - pad, d + pad + 1):
            out[yy][xx] = color
    for yy in range(r, b + 1):
        out[yy][c : d + 1] = a[yy][c : d + 1]
    return out
