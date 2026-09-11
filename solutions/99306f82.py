def bounds(points):
    rows, cols = zip(*points)
    return min(rows), min(cols), max(rows), max(cols)


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = [row[:] for row in a]
    r, c, b, d = bounds(
        [(y, x) for y, row in enumerate(a) for x, value in enumerate(row) if value == 1]
    )
    palette = [
        a[y][x]
        for y, row in enumerate(a)
        for x, value in enumerate(row)
        if value not in (0, 1)
        if not (r <= y <= b and c <= x <= d)
    ]
    for y in range(r + 1, b):
        for x in range(c + 1, d):
            out[y][x] = palette[
                min(min(y - r - 1, b - y - 1, x - c - 1, d - x - 1), len(palette) - 1)
            ]
    return out
