def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = copy(g)
    groups = {
        c: [(r, k) for r, row in enumerate(g) for k, v in enumerate(row) if v == c]
        for c in {v for row in g for v in row if v}
    }
    for vertical in (False, True):
        for color, ps in groups.items():
            if len(ps) != 2:
                raise ValueError("candidate does not contain exactly two points per color")
            (r, c), (a, b) = ps
            if vertical and c == b:
                for i in range(min(r, a), max(r, a) + 1):
                    out[i][c] = color
            elif not vertical and r == a:
                for j in range(min(c, b), max(c, b) + 1):
                    out[r][j] = color
    return out
