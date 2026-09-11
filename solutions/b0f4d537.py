def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    sep = next(c for c in range(w) if all(g[r][c] == 5 for r in range(h)))
    parts = ([row[:sep] for row in g], [row[sep + 1 :] for row in g])
    target = next(p for p in parts if 4 in sum(p, []))
    template = next(p for p in parts if 4 not in sum(p, []))
    template = [row for row in template if any(v != 5 for v in row)]
    tr = [r for r, row in enumerate(template) if all(v != 0 for v in row)]
    tc = [c for c in range(len(template[0])) if all(row[c] != 0 for row in template)]
    rr = [r for r in range(h) if target[r][0] == 4 or target[r][-1] == 4]
    cc = [c for c in range(len(target[0])) if target[0][c] == 4 or target[-1][c] == 4]
    if len(rr) != len(tr) or len(cc) != len(tc):
        raise ValueError("Line counts differ")
    out = [[0] * len(target[0]) for _ in range(h)]
    for r, sr in zip(rr, tr):
        color = next(template[sr][c] for c in range(len(template[0])) if c not in tc)
        for c in range(len(out[0])):
            out[r][c] = color
    for c, sc in zip(cc, tc):
        color = next(template[r][sc] for r in range(len(template)) if r not in tr)
        for r in range(h):
            out[r][c] = color
    for r, sr in zip(rr, tr):
        for c, sc in zip(cc, tc):
            out[r][c] = template[sr][sc]
    return out
