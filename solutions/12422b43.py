def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    out = copy(g)
    n = sum(row[0] == 5 for row in g)
    end = max((r for r, row in enumerate(g) if any(row[1:])))
    pattern = [row[1:] for row in g[:n]]
    for r in range(end + 1, len(g)):
        out[r][1:] = pattern[(r - end - 1) % n]
    return out
