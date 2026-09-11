def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = cp(g)
    out = cp(g)
    r0 = min((r for r, row in enumerate(g) if any(row)))
    c0 = min((c for row in g for c, v in enumerate(row) if v))
    n = 4
    ref = [row[c0 : c0 + n] for row in g[r0 : r0 + n]]
    for vr, hc in ((0, 1), (1, 0), (1, 1)):
        pattern = [
            [ref[n - 1 - r if vr else r][n - 1 - c if hc else c] for c in range(n)]
            for r in range(n)
        ]
        mapping = {}
        for r in range(n):
            for c in range(n):
                v = g[r0 + vr * n + r][c0 + hc * n + c]
                if v:
                    key = pattern[r][c]
                    if key in mapping and mapping[key] != v:
                        raise ValueError("Conflicting color hints")
                    mapping[key] = v
        for r in range(n):
            for c in range(n):
                out[r0 + vr * n + r][c0 + hc * n + c] = mapping.get(pattern[r][c], 0)
    return out
