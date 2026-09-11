def pts(g, color):
    return {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color}


def cp(g):
    return [list(r) for r in g]


def paint(g, p, color):
    for r, c in p:
        if 0 <= r < len(g) and 0 <= c < len(g[0]):
            g[r][c] = color
    return g


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    edges = []
    if len(set(g[0])) == 1:
        edges.append(("up", g[0][0]))
    if len(set(g[-1])) == 1:
        edges.append(("down", g[-1][0]))
    if len({row[0] for row in g}) == 1:
        edges.append(("left", g[0][0]))
    if len({row[-1] for row in g}) == 1:
        edges.append(("right", g[0][-1]))
    o = cp(g)
    for r, c in pts(g, 1):
        choices = [
            ({"up": r, "down": h - 1 - r, "left": c, "right": w - 1 - c}[side], side, color)
            for side, color in edges
            if color not in (0, 1)
        ]
        _, side, color = min(choices)
        dr, dc = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}[side]
        paint(o, {(r + dr, c + dc)}, color)
    return o
