def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    ((r, c),) = points(g, 1)
    ((a, b),) = points(g, 2)
    out = cp(g)

    def sign(v):
        return (v > 0) - (v < 0)

    while max(abs(a - r), abs(b - c)) > 1:
        dr, dc = (sign(a - r), sign(b - c))
        if abs(a - r) == 1:
            dr = 0
        if abs(b - c) == 1:
            dc = 0
        r += dr
        c += dc
        out[r][c] = 3
    return out
