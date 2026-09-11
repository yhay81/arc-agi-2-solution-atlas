def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    out = copy(g)
    h, w = (len(g), len(g[0]))
    points = [(r, v) for r, row in enumerate(g) for v in row if v]
    for r in range(h):
        color = min(points, key=lambda p: abs(p[0] - r))[1]
        out[r][0] = out[r][-1] = color
    for r, color in points:
        out[r] = [color] * w
    out[0] = [min(points)[1]] * w
    out[-1] = [max(points)[1]] * w
    return out
