def solve(grid):
    g = grid
    marks = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 5]
    (a, b), (c, d) = marks
    clean = [[8 if v == 5 else v for v in row] for row in g]
    if a != c:
        n = len(g) // abs(c - a)
        return clean[:n] if (a + c) / 2 < len(g) / 2 else clean[-n:]
    n = len(g[0]) // abs(d - b)
    return [row[:n] if (b + d) / 2 < len(g[0]) / 2 else row[-n:] for row in clean]
