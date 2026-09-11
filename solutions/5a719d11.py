from collections import Counter


def mode(values):
    return Counter(values).most_common(1)[0][0]


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
    rows = runs([r for r, row in enumerate(a) if any(row)])
    cols = runs([c for c in range(len(a[0])) if any(row[c] for row in a)])
    if not (len(cols) == 2):
        raise ValueError("task assumptions are not satisfied")
    out = [row[:] for row in a]
    for rs in rows:
        panels = [[[a[r][c] for c in cs] for r in rs] for cs in cols]
        bgs = [mode([v for row in p for v in row]) for p in panels]
        for i, cs in enumerate(cols):
            for y, r in enumerate(rs):
                for x, c in enumerate(cs):
                    out[r][c] = bgs[1 - i] if panels[1 - i][y][x] != bgs[1 - i] else bgs[i]
    return out
