def bounds(points):
    rows, cols = zip(*points)
    return min(rows), min(cols), max(rows), max(cols)


def solve(grid):
    a = grid
    points = [(r, c) for r, row in enumerate(a) for c, value in enumerate(row) if value]
    r, c, _, _ = bounds(points)
    return [row[c : c + 4] for row in a[r : r + 4]]
