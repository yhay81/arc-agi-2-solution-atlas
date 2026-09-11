def bounds(points):
    rows, cols = zip(*points)
    return min(rows), min(cols), max(rows), max(cols)


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    r, c, b, d = bounds(
        [(y, x) for y, row in enumerate(a) for x, value in enumerate(row) if value != 0]
    )
    if not (b - r == 2 and d - c == 2):
        raise ValueError("task assumptions are not satisfied")
    out = [row[:] for row in a]
    cy, cx = (r + 1, c + 1)
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if (dy, dx) == (0, 0):
                continue
            color = a[cy + dy][cx + dx]
            y, x = (cy + dy, cx + dx)
            while 0 <= y < len(a) and 0 <= x < len(a[0]):
                out[y][x] = color
                y += dy
                x += dx
    return out
