def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    out = copy(g)
    reach = -1
    for c in range(w):
        ps = [r for r, row in enumerate(g) if row[c]]
        if not ps:
            continue
        color = g[ps[-1]][c]
        height = len(ps)
        if ps != list(range(h - height, h)) or len({g[r][c] for r in ps}) != 1:
            raise ValueError("contains a shape other than a vertical bar")
        if color == 1 or c <= reach:
            for r in ps:
                out[r][c] = 0
            for b in range(c, min(w, c + height)):
                out[-1][b] = color
            reach = c + height
    return out
