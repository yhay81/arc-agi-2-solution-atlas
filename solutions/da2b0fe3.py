def cp(g):
    return [row[:] for row in g]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    cells = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != 0]
    a, b, c, d = bbox(cells)
    out = cp(g)
    targets = []
    for col in range(c + 1, d):
        if all(g[r][col] == 0 for r in range(a, b + 1)):
            targets.append(("v", col))
    for r in range(a + 1, b):
        if all(g[r][col] == 0 for col in range(c, d + 1)):
            targets.append(("h", r))
    if len(targets) != 1:
        raise ValueError("Ambiguous full cut")
    axis, p = targets[0]
    if axis == "v":
        for row in out:
            row[p] = 3
    else:
        out[p] = [3] * len(g[0])
    return out
