def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = cp(g)
    counts = [sum(row[c] == 1 for row in g) for c in range(len(g[0]))]
    out = cp(g)
    for c, n in enumerate(counts):
        if c in (counts.index(max(counts)), len(counts) - 1 - counts[::-1].index(min(counts))):
            for r in range(len(g)):
                if g[r][c] == 1:
                    out[r][c] = 9 if n == max(counts) else 4
    return out
