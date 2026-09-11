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
    color = next(v for row in g for v in row if v not in (0, 1, 4))
    pts = points(g, color)
    a, b, c, d = bbox(pts)
    scale = max(b - a + 1, d - c + 1) // 3
    if scale < 1:
        raise ValueError("Reference scale mismatch")
    pattern = {(int((r - a) // scale), int((col - c) // scale)) for r, col in pts}
    out = cp(g)
    for r in range(0, len(g) - 2, 4):
        for col in range(0, len(g[0]) - 2, 4):
            if all((g[r + dr][col + dc] == 1 for dr, dc in pattern)):
                for dr, dc in pattern:
                    out[r + dr][col + dc] = color
    return out
