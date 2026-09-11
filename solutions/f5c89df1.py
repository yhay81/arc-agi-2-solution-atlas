def solve(grid):
    g = grid
    r, c = next(((r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 3))
    offsets = [(a - r, b - c) for a, row in enumerate(g) for b, v in enumerate(row) if v == 8]
    out = [[0] * len(g[0]) for _ in g]
    for a, row in enumerate(g):
        for b, v in enumerate(row):
            if v == 2:
                for dr, dc in offsets:
                    if 0 <= a + dr < len(g) and 0 <= b + dc < len(g[0]):
                        out[a + dr][b + dc] = 8
    return out
