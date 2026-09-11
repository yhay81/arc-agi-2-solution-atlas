def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    out = copy(g)
    red = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 2}
    for r, c in red:
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if (r + dr, c + dc) in red:
                continue
            ray = []
            rr, cc = (r + dr, c + dc)
            while 0 <= rr < len(g) and 0 <= cc < len(g[0]):
                ray.append((rr, cc))
                rr += dr
                cc += dc
            if all((g[a][b] in (0, 2) for a, b in ray)):
                for a, b in ray:
                    out[a][b] = 2
    return out
