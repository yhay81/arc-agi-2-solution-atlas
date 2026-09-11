def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    seps = [c for c in range(w) if all(g[r][c] == 0 for r in range(h))]
    bounds = [-1] + seps + [w]
    panels = [[row[left + 1 : right] for row in g] for left, right in zip(bounds, bounds[1:])]
    panels.sort(key=lambda p: sum(v == 0 for row in p for v in row))
    out = []
    for r in range(h):
        row = []
        for i, p in enumerate(panels):
            if i:
                row.append(0)
            row += p[r]
        out.append(row)
    return out
