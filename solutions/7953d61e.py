def rot90(g):
    return [list(row) for row in zip(*g[::-1])]


def solve(grid):
    g = grid
    r90 = rot90(g)
    r180 = rot90(r90)
    r270 = rot90(r180)
    return [a + b for a, b in zip(g, r270)] + [a + b for a, b in zip(r180, r90)]
