from collections import Counter


def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = copy(g)
    n = sum(v == 8 for v in g[0])
    wall = next((r for r, row in enumerate(g) if all(v == 5 for v in row)))
    row = next(row for row in g[wall + 1 :] if any(row))
    counts = Counter(row)
    for c, v in enumerate(row):
        if counts[v] == n:
            for r in range(wall - n, wall):
                out[r][c] = v
    return out
