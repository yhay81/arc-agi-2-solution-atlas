def solve(grid):
    points = [(r, c, v) for r, row in enumerate(grid) for c, v in enumerate(row) if v not in (0, 5)]
    if len(points) != 1:
        raise ValueError("Expected one colored seed point")
    pr, pc, color = points[0]
    out = [row[:] for row in grid]
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == 0 and (r - pr) % 2 == 0 and (c - pc) % 2 == 0:
                out[r][c] = color
    return out
