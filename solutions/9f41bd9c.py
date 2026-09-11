def bounds(points):
    rs, cs = zip(*points)
    return min(rs), min(cs), max(rs), max(cs)


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = [row[:] for row in a]
    p5 = [(y, x) for y, row in enumerate(a) for x, v in enumerate(row) if v == 5]
    for y, x in p5:
        out[y][x] = 1
    r, c, b, d = bounds(p5)
    h, w = len(a), len(a[0])
    right = c > w // 2
    full = [y for y in range(r, b + 1) if all(a[y][x] == 5 for x in range(c, d + 1))]
    first = max(full) + 1
    newc = w - 1 - d
    newd = w - 1 - c
    for y, x in p5:
        xx = w - 1 - x + (max(0, y - first) if right else -max(0, y - first))
        if 0 <= xx < w:
            out[y][xx] = 5
    wall = next(y for y, row in enumerate(a) if all(v == 6 for v in row))
    k = wall - first
    if right:
        for x in range(newc + k, w):
            out[wall][x] = 9
    else:
        for x in range(newd - k + 1):
            out[wall][x] = 9
    return out
