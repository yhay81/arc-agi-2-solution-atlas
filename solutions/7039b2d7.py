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
    bg = mode(value for row in a for value in row)
    rows = runs(r for r, row in enumerate(a) if any(value == bg for value in row))
    cols = runs(c for c in range(len(a[0])) if any(row[c] == bg for row in a))
    return [[bg] * len(cols) for _ in rows]
