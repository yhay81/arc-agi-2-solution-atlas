def bounds(points):
    return (
        min(r for r, c in points),
        max(r for r, c in points),
        min(c for r, c in points),
        max(c for r, c in points),
    )


def solve(grid):
    frame = {(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 2}
    gray = {(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 5}
    if not frame or not gray:
        raise ValueError("Expected red frame and gray pattern")
    top, bottom, left, right = bounds(frame)
    a, b, c, d = bounds(gray)
    out = [row[:] for row in grid]
    for r in range(top + 1, bottom):
        for col in range(left + 1, right):
            if not (a <= r <= b and c <= col <= d):
                out[r][col] = 2
    return out
