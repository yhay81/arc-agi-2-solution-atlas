def bounds(points):
    rows, cols = zip(*points)
    return min(rows), min(cols), max(rows), max(cols)


def solve(grid):
    a = grid
    ps = [(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == 8]
    r, c, b, d = bounds(ps)
    cy, cx = ((r + b) // 2, (c + d) // 2)
    patch = [[0] * 3 for _ in range(3)]
    for y, x in ps:
        patch[y - cy + 1][x - cx + 1] = 8
    count4 = sum(v == 4 for row in a for v in row)
    return [row * count4 for row in patch]
