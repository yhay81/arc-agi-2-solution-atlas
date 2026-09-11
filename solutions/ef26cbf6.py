def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    out = cp(g)
    h, w = (len(g), len(g[0]))
    seprows = [r for r, row in enumerate(g) if all(v == 4 for v in row)]
    sepcols = [c for c in range(w) if all(g[r][c] == 4 for r in range(h))]

    def intervals(n, seps):
        bounds = [-1] + seps + [n]
        return [(a + 1, b) for a, b in zip(bounds, bounds[1:]) if a + 1 < b]

    rowbands = intervals(h, seprows)
    colbands = intervals(w, sepcols)

    def apply(groups):
        changes = []
        for cells in groups:
            marks = [g[r][c] for r, c in cells if g[r][c] not in (0, 1, 4)]
            blues = [(r, c) for r, c in cells if g[r][c] == 1]
            if blues and len(set(marks)) == 1:
                changes.append((blues, marks[0]))
            elif blues or marks:
                return None
        return changes

    rowgroups = [
        [(r, c) for r in range(a, b) for c in range(w) if c not in sepcols] for a, b in rowbands
    ]
    colgroups = [
        [(r, c) for r in range(h) if r not in seprows for c in range(a, b)] for a, b in colbands
    ]
    changes = apply(rowgroups)
    if changes is None:
        changes = apply(colgroups)
    if changes is None:
        raise ValueError("Legend pairing is ambiguous")
    for cells, color in changes:
        for r, c in cells:
            out[r][c] = color
    return out
