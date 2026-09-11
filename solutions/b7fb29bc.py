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
    r, c, b, d = bounds([(y, x) for y, row in enumerate(a) for x, v in enumerate(row) if v == 3])
    inside = [(y, x) for y in range(r + 1, b) for x in range(c + 1, d) if a[y][x] == 3]
    if not (len(inside) == 1):
        raise ValueError("task assumptions are not satisfied")
    cy, cx = inside[0]
    out = [row[:] for row in a]
    for y in range(r + 1, b):
        for x in range(c + 1, d):
            if out[y][x] == 0:
                out[y][x] = 4 if max(abs(y - cy), abs(x - cx)) % 2 else 2
    return out
