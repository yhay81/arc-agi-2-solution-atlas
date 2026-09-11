def bounds(points):
    return (
        min(r for r, _ in points),
        min(c for _, c in points),
        max(r for r, _ in points),
        max(c for _, c in points),
    )


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    sizes = []
    for color in set(v for row in a for v in row) - {0}:
        r, c, b, d = bounds(
            [(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == color]
        )
        sizes.append((max(b - r, d - c) + 1, color))
    sizes.sort()
    n = max(x[0] for x in sizes)
    out = [[0] * n for _ in range(n)]
    for size, color in reversed(sizes):
        s = (n - size) // 2
        for r in range(s, s + size):
            for c in range(s, s + size):
                out[r][c] = color
    return out
