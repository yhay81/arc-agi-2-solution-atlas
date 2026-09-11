def pts(g, color):
    return {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color}


def pal(g):
    return set(v for r in g for v in r)


def box(p):
    return (
        min((r for r, c in p)),
        max((r for r, c in p)),
        min((c for r, c in p)),
        max((c for r, c in p)),
    )


def solve(grid):
    g = grid
    items = [(box(pts(g, v))[1] - box(pts(g, v))[0] + 1, v) for v in pal(g) - {0}]
    items.sort(reverse=True)
    return [[v if r < n else 0 for n, v in items] for r in range(items[0][0])]
