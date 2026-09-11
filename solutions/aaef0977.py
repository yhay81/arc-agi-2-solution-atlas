def solve(grid):
    a = grid
    points = [(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v != 7]
    if len(points) != 1:
        raise ValueError("Expected one colored seed")
    r, c = points[0]
    cycle = [0, 5, 2, 8, 9, 6, 1, 3, 4]
    index = cycle.index(a[r][c])
    return [
        [cycle[(index + abs(y - r) + abs(x - c)) % len(cycle)] for x in range(len(a[0]))]
        for y in range(len(a))
    ]
