def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    dividers = [c for c in range(w) if all(g[r][c] == 0 for r in range(h))]
    bounds = [-1] + dividers + [w]
    panels = [[row[a + 1 : b] for row in g] for a, b in zip(bounds, bounds[1:])]
    if len({len(p[0]) for p in panels}) != 1:
        raise ValueError("Unequal panel widths")
    panels.sort(key=lambda p: sum(v == 0 for row in p for v in row), reverse=True)
    out = []
    for r in range(h):
        row = []
        for i, p in enumerate(panels):
            if i:
                row.append(0)
            row.extend(p[r])
        out.append(row)
    return out
