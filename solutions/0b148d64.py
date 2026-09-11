def solve(grid):
    h, w = len(grid), len(grid[0])
    sr = [r for r in range(h) if all(v == 0 for v in grid[r])]
    sc = [c for c in range(w) if all(grid[r][c] == 0 for r in range(h))]

    def bands(n, seps):
        e = [-1] + seps + [n]
        return [(a + 1, b) for a, b in zip(e, e[1:]) if b > a + 1]

    rs, cs = bands(h, sr), bands(w, sc)
    panels = [[row[l:r] for row in grid[t:b]] for t, b in rs for l, r in cs]
    if len(panels) < 2:
        return [r[:] for r in grid]
    sig = [tuple(sorted({v for row in p for v in row if v})) for p in panels]
    ix = [i for i, s in enumerate(sig) if s and sig.count(s) == 1]
    return panels[ix[0]] if len(ix) == 1 else [r[:] for r in grid]
