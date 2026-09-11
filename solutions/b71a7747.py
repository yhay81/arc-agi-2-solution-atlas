def solve(grid):
    g = grid
    g = [row[:] for row in g]
    colors = sorted(set(v for row in g for v in row))
    candidates = []
    for i, x in enumerate(colors):
        for y in colors[i + 1 :]:
            ps = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v in (x, y)}
            rs = sorted({r for r, c in ps})
            cs = sorted({c for r, c in ps})
            if (
                len(ps) == len(rs) * len(cs)
                and len(rs) < len(g)
                and (len(cs) < len(g[0]))
                and (len(rs) > 2)
                and (len(cs) > 2)
            ):
                candidates.append((len(ps), rs, cs))
    if len(candidates) != 1:
        raise ValueError("Tile colors ambiguous")
    _, rs, cs = candidates[0]
    return [[g[r][c] for c in cs] for r in rs]
