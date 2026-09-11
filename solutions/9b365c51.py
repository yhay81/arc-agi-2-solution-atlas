def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    colors = [
        g[0][c]
        for c in range(w)
        if g[0][c] not in (0, 8) and all(g[r][c] == g[0][c] for r in range(h))
    ]
    groups = []
    for c in range(w):
        rows = tuple(r for r in range(h) if g[r][c] == 8)
        if not rows:
            continue
        if groups and groups[-1][0] == rows and (groups[-1][1][-1] == c - 1):
            groups[-1][1].append(c)
        else:
            groups.append((rows, [c]))
    if len(groups) != len(colors):
        raise ValueError("Legend and rectangles differ")
    out = [[0] * w for _ in g]
    for color, (rows, cols) in zip(colors, groups):
        for r in rows:
            for c in cols:
                out[r][c] = color
    return out
