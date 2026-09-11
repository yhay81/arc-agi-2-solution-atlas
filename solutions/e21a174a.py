def bounds(points):
    rows, cols = zip(*points)
    return min(rows), min(cols), max(rows), max(cols)


def solve(grid):
    a = grid
    out = [[0] * len(a[0]) for _ in a]
    for color in {v for row in a for v in row if v}:
        ps = [(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == color]
        r, c, b, d = bounds(ps)
        shift = len(a) - 1 - b - r
        for y, x in ps:
            out[y + shift][x] = color
    return out
