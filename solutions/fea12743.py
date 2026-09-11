from itertools import combinations


def paint(g, p, color):
    for r, c in p:
        if 0 <= r < len(g) and 0 <= c < len(g[0]):
            g[r][c] = color
    return g


def shift(p, dr, dc):
    return {(r + dr, c + dc) for r, c in p}


def cp(g):
    return [list(r) for r in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    objs = []
    masks = []
    for r in range(1, len(g), 5):
        for c in range(1, len(g[0]), 5):
            p = {
                (r + i, c + j)
                for i in range(4)
                for j in range(4)
                if r + i < len(g) and c + j < len(g[0]) and g[r + i][c + j]
            }
            objs.append(p)
            masks.append(shift(p, -r, -c))
    o = cp(g)
    for i, j in combinations(range(len(objs)), 2):
        for k in range(len(objs)):
            if (
                k not in (i, j)
                and masks[i] | masks[j] == masks[k]
                and (masks[k] != masks[i])
                and (masks[k] != masks[j])
            ):
                paint(o, objs[i] | objs[j], 8)
                paint(o, objs[k], 3)
                return o
    return o
