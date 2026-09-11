from collections import Counter


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    pending = set(points(g, 2))
    groups = []
    while pending:
        p = pending.pop()
        group = {p}
        queue = [p]
        for r, c in queue:
            near = {q for q in pending if max(abs(q[0] - r), abs(q[1] - c)) <= 2}
            pending -= near
            group |= near
            queue.extend(near)
        groups.append(group)
    shapes = []
    for o in groups:
        a, b, c, d = bbox(o)
        shapes.append(tuple(sorted(((r - a, col - c) for r, col in o))))
    counts = Counter(shapes)
    rare = [i for i, s in enumerate(shapes) if counts[s] == 1]
    if len(rare) != 1:
        raise ValueError("No unique red pattern")
    o = groups[rare[0]]
    a, b, c, d = bbox(o)
    return [row[c - 1 : d + 2] for row in g[a - 1 : b + 2]]
