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
    g = cp(g)
    w = len(g[0])
    divs = [c for c in range(w) if all(row[c] == 5 for row in g)]
    if len(divs) != 1:
        raise ValueError("Expected gray split")
    c = divs[0]
    left = [row[:c] for row in g]
    right = [row[c + 1 :] for row in g]
    ps = [(r, col) for r, row in enumerate(right) for col, v in enumerate(row) if v != 0]
    holes = [(r, col) for r, row in enumerate(left) for col, v in enumerate(row) if v == 0]
    if not ps:
        return left
    if set(ps) == set(holes):
        a, b, l, d = bbox(ps)
        aa, bb, ll, dd = bbox(holes)
        out = cp(left)
        for r, col in ps:
            out[r - a + aa][col - l + ll] = right[r][col]
        return out
    return left
