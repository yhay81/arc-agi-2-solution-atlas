def runs(indices):
    groups = []
    for n in indices:
        if not groups or n != groups[-1][-1] + 1:
            groups.append([])
        groups[-1].append(int(n))
    return groups


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = [row[:] for row in a]
    rows = runs([r for r, row in enumerate(a) if not all(v == 3 for v in row)])
    cols = runs([c for c in range(len(a[0])) if not all(row[c] == 3 for row in a)])
    for i, rs in enumerate(rows):
        for j, cs in enumerate(cols):
            color = {
                (0, 0): 2,
                (0, len(cols) - 1): 4,
                (len(rows) - 1, 0): 1,
                (len(rows) - 1, len(cols) - 1): 8,
            }.get((i, j))
            if 0 < i < len(rows) - 1 and 0 < j < len(cols) - 1:
                color = 7
            if color is not None:
                for r in rs:
                    for c in cs:
                        out[r][c] = color
    return out
