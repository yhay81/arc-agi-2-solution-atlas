from collections import Counter


def mode(values):
    return Counter(values).most_common(1)[0][0]


def bounds(points):
    rows, cols = zip(*points)
    return min(rows), min(cols), max(rows), max(cols)


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    color = mode([v for row in a for v in row if v != 0])
    r, c, b, d = bounds(
        [(y, x) for y, row in enumerate(a) for x, v in enumerate(row) if v == color]
    )
    if b - r > d - c:
        result = solve([list(row) for row in zip(*a)])
        return [list(row) for row in zip(*result)]
    out = [row[:] for row in a]
    for col in range(len(a[0])):
        band = [y for y in range(len(a)) if a[y][col] == color]
        if not len(band):
            continue
        top, bottom = min(band), max(band)
        up = [y for y in range(top) if a[y][col] not in (0, color)]
        down = [y for y in range(bottom + 1, len(a)) if a[y][col] not in (0, color)]
        if len(up) == len(down) == 1:
            above, below = (up[0], down[0])
            out[above][col] = 0
            out[below][col] = 0
            out[top - 1][col] = a[below][col]
            out[bottom + 1][col] = a[above][col]
    return out
