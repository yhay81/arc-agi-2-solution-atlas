def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    blocks = [
        (r, c)
        for r in range(h - 1)
        for c in range(w - 1)
        if all(g[r + dr][c + dc] == 8 for dr in (0, 1) for dc in (0, 1))
    ]
    bands = []
    for r in sorted({r for r, c in blocks}):
        cs = [c for rr, c in blocks if rr == r]
        if len(cs) != 2:
            raise ValueError("Expected two anchors per strip")
        a, b = cs
        bands.extend([row[a + 2 : b] for row in g[r : r + 2]])
    if len({len(row) for row in bands}) != 1:
        raise ValueError("Unequal strip widths")
    return bands
