def bounds(points):
    rows, cols = zip(*points)
    return min(rows), min(cols), max(rows), max(cols)


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    r, c, b, d = bounds([(y, x) for y, row in enumerate(a) for x, v in enumerate(row) if v == 5])
    out = [row[:] for row in a]
    colors = sorted({a[y][x] for y in range(r + 1, b) for x in range(c + 1, d)} - {0, 5})
    if not (len(colors) == 2):
        raise ValueError("task assumptions are not satisfied")
    for y in range(r + 1, b):
        for x in range(c + 1, d):
            if a[y][x] == colors[0]:
                out[y][x] = colors[1]
            elif a[y][x] == colors[1]:
                out[y][x] = colors[0]
    return out
