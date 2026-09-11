def cp(g):
    return [row[:] for row in g]


def panels(g, separator):
    h, w = (len(g), len(g[0]))
    rs = [-1] + [r for r, row in enumerate(g) if all(v == separator for v in row)] + [h]
    cs = [-1] + [c for c in range(w) if all(row[c] == separator for row in g)] + [w]
    return [
        (a + 1, c + 1, [row[c + 1 : d] for row in g[a + 1 : b]])
        for a, b in zip(rs, rs[1:])
        for c, d in zip(cs, cs[1:])
        if b > a + 1 and d > c + 1
    ]


def solve(grid):
    g = grid
    g = cp(g)
    ps = panels(g, 0)
    refs = [p for r, c, p in ps if set(v for row in p for v in row) - {0, 7}]
    if len(refs) != 1:
        raise ValueError("Expected one colored template")
    ref = refs[0]
    out = cp(g)
    for r, c, p in ps:
        if any(v == 0 for row in p for v in row):
            if len(p) != len(ref) or len(p[0]) != len(ref[0]):
                raise ValueError("Unequal panel shape")
            for dr, row in enumerate(ref):
                for dc, value in enumerate(row):
                    out[r + dr][c + dc] = value
    return out
