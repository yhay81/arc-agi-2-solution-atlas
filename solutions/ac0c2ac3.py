def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    cr, cc = (h // 2, w // 2)
    byradius = {}
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            if v == 7:
                continue
            distance = max(abs(r - cr), abs(c - cc))
            if distance in byradius and byradius[distance] != v:
                raise ValueError("Conflicting ring colors")
            byradius[distance] = v
    return [[byradius[max(abs(r - cr), abs(c - cc))] for c in range(w)] for r in range(h)]
