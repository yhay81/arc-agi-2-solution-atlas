def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def solve(grid):
    g = grid
    g = cp(g)
    out = cp(g)
    a, b, c, d = bbox(points(g, 8))
    size = 4
    for r0 in range(a, b + 1, size):
        for c0 in range(c, d + 1, size):
            if not any(
                0 <= r < len(g) and 0 <= col < len(g[0]) and (g[r][col] == 8)
                for r in range(r0, r0 + size)
                for col in range(c0, c0 + size)
            ):
                continue
            for r in range(r0, r0 + size):
                for col in range(c0, c0 + size):
                    if 0 <= r < len(g) and 0 <= col < len(g[0]) and (g[r][col] == 0):
                        out[r][col] = 2
    return out
