from collections import Counter


def mode(values):
    return Counter(values).most_common(1)[0][0]


def bounds(points):
    rs, cs = zip(*points)
    return min(rs), min(cs), max(rs), max(cs)


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = [row[:] for row in a]
    for col in set(v for row in a for v in row) - {6, 7}:
        ps = [(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == col]
        r, c, b, d = bounds(ps)
        cy = mode([r for r, _ in ps])
        cx = mode([c for _, c in ps])
        if b - r > d - c:
            short_top = cy - r < b - cy
            out[0][cx] = col if short_top else 0
            out[-1][cx] = 0 if short_top else col
        else:
            short_left = cx - c < d - cx
            out[cy][0] = col if short_left else 0
            out[cy][-1] = 0 if short_left else col
    return out
