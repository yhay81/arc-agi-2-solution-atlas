def bounds(points):
    rows, cols = zip(*points)
    return min(rows), min(cols), max(rows), max(cols)


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = [row[:] for row in a]
    for color in {value for row in a for value in row} - {0, 8}:
        ps = [(r, c) for r, row in enumerate(a) for c, value in enumerate(row) if value == color]
        p = [(round(r / 4) * 4, round(c / 4) * 4) for r, c in ps]
        r, c, b, d = bounds(p)
        for y in range(r, b + 1):
            out[y][c] = color
            out[y][d] = color
        for x in range(c, d + 1):
            out[r][x] = color
            out[b][x] = color
        for y in range(r + 2, b, 4):
            for x in range(c + 2, d, 4):
                out[y][x] = color
    return out
