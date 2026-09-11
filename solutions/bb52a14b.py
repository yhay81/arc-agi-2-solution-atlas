def bbox(ps):
    return (
        min((r for r, c in ps)),
        min((c for r, c in ps)),
        max((r for r, c in ps)),
        max((c for r, c in ps)),
    )


def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    out = copy(g)
    ps = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 4]
    a, b, z, d = bbox(ps)
    patch = [row[b : d + 1] for row in g[a : z + 1]]
    h, w = (len(patch), len(patch[0]))
    for r in range(len(g) - h + 1):
        for c in range(len(g[0]) - w + 1):
            if all(
                (
                    g[r + x][c + y] == v
                    for x, row in enumerate(patch)
                    for y, v in enumerate(row)
                    if v != 4
                )
            ):
                for x, row in enumerate(patch):
                    for y, v in enumerate(row):
                        if v == 4:
                            out[r + x][c + y] = 4
    return out
