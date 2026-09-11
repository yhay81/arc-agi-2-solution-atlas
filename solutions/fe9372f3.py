def solve(grid):
    a = grid
    points = [(r, c) for r, row in enumerate(a) for c, value in enumerate(row) if value == 2]
    r = sum(y for y, _ in points) // len(points)
    c = sum(x for _, x in points) // len(points)
    out = [row[:] for row in a]
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if (dy, dx) == (0, 0):
                continue
            for n in range(1, max(len(a), len(a[0]))):
                y, x = (r + dy * n, c + dx * n)
                if 0 <= y < len(a) and 0 <= x < len(a[0]) and a[y][x] != 2:
                    out[y][x] = 1 if dy and dx else 8 if (n - 2) % 3 < 2 else 4
    return out
