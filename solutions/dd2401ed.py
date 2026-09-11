def cp(g):
    return [list(r) for r in g]


def solve(grid):
    g = grid
    old = next(c for c in range(len(g[0])) if all(row[c] == 5 for row in g))
    new = 2 * old + 1
    if not (new < len(g[0])):
        raise ValueError("task assumptions are not satisfied")
    odd = sum(row[:old].count(1) for row in g) % 2
    o = cp(g)
    for row in o:
        row[old] = 0
        row[new] = 5
        if odd:
            for c in range(new):
                if row[c] == 2:
                    row[c] = 1
    return o
