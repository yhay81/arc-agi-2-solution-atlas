def bounds(points):
    return (
        min(r for r, _ in points),
        min(c for _, c in points),
        max(r for r, _ in points),
        max(c for _, c in points),
    )


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    r, c, b, d = bounds([(y, x) for y, row in enumerate(a) for x, v in enumerate(row) if v == 1])
    out = [[2 if v == 1 else 7 if v == 9 else v for v in row] for row in a]
    ps = [(y, x) for y, row in enumerate(a) for x, v in enumerate(row) if v == 9]
    dist = [max(r - y, 0, y - b) + max(c - x, 0, x - d) for y, x in ps]
    closest = dist.index(min(dist))
    for i, (y, x) in enumerate(ps):
        pad = 0 if i == closest else 1
        out[min(max(y, r - pad), b + pad)][min(max(x, c - pad), d + pad)] = 9
    return out
