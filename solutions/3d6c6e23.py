from math import isqrt


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = [[0] * len(g[0]) for _ in g]
    for center in range(len(g[0])):
        values = [row[center] for row in g if row[center]]
        if not values:
            continue
        n = isqrt(len(values))
        if n * n != len(values):
            raise ValueError("the number of points in a row is not a perfect square")
        pos = 0
        for j in range(n):
            for c in range(center - j, center + j + 1):
                out[len(g) - n + j][c] = values[pos]
                pos += 1
    return out
