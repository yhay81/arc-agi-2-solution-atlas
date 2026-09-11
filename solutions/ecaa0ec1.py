import itertools as itertools


def bounds(points):
    rows, cols = zip(*points)
    return min(rows), min(cols), max(rows), max(cols)


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    points = {(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == 4}
    groups = []
    for triple in itertools.combinations(points, 3):
        r, c, b, d = bounds(triple)
        if b - r == 2 and d - c == 2 and (set(triple) <= {(r, c), (r, d), (b, c), (b, d)}):
            groups.append((set(triple), (r + 1, c + 1)))
    if not (len(groups) == 1):
        raise ValueError("task assumptions are not satisfied")
    group, target = groups[0]
    old = next(iter(points - group))
    colored = [(y, x) for y, row in enumerate(a) for x, value in enumerate(row) if value in (1, 8)]
    r, c, b, d = bounds(colored)
    center = ((r + b) // 2, (c + d) // 2)
    v = (old[0] - center[0], old[1] - center[1])
    goal = (target[0] - center[0], target[1] - center[1])
    for k in range(4):
        if v == goal:
            break
        v = (-v[1], v[0])
    else:
        raise ValueError("handle does not rotate to target")
    out = [[0 if value == 4 else value for value in row] for row in a]
    block = [row[c : d + 1] for row in a[r : b + 1]]
    for _ in range(k):
        block = [list(row) for row in zip(*block)][::-1]
    for y, row in enumerate(block, r):
        for x, value in enumerate(row, c):
            out[y][x] = value
    out[target[0]][target[1]] = 4
    return out
