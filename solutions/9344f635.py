def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    out = [[7] * w for _ in range(h)]
    for c in range(w):
        colors = {g[r][c] for r in range(h - 1) if g[r][c] == g[r + 1][c] != 7}
        if len(colors) > 1:
            raise ValueError("Conflicting vertical markers")
        if colors:
            color = next(iter(colors))
            for r in range(h):
                out[r][c] = color
    for r, row in enumerate(g):
        colors = {row[c] for c in range(w - 1) if row[c] == row[c + 1] != 7}
        if len(colors) > 1:
            raise ValueError("Conflicting horizontal markers")
        if colors:
            out[r] = [next(iter(colors))] * w
    return out
