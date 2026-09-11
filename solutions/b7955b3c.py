from collections import Counter


def mode(values):
    return Counter(values).most_common(1)[0][0]


def bounds(points):
    rows, cols = zip(*points)
    return min(rows), min(cols), max(rows), max(cols)


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    border = a[0] + a[-1] + [row[0] for row in a] + [row[-1] for row in a]
    bg = mode(border)
    cs = {v for row in a for v in row} - {8, bg}
    boxes = {
        c: bounds([(r, col) for r, row in enumerate(a) for col, v in enumerate(row) if v == c])
        for c in cs
    }
    edges = {c: set() for c in cs}
    for c, (y, x, v, u) in boxes.items():
        edges[c] = ({a[r][col] for r in range(y, v + 1) for col in range(x, u + 1)} & cs) - {c}
    remaining = set(cs)
    order = []
    while remaining:
        bottom = [c for c in remaining if not any(c in edges[d] for d in remaining - {c})]
        if not (bottom):
            raise ValueError("cyclic occlusions")
        c = min(bottom)
        order.append(c)
        remaining.remove(c)
    o = [row[:] for row in a]
    for r in range(len(o)):
        for col in range(len(o[0])):
            if o[r][col] == 8:
                o[r][col] = bg
    for c in order:
        y, x, v, u = boxes[c]
        for r in range(y, v + 1):
            for col in range(x, u + 1):
                if a[r][col] == 8:
                    o[r][col] = c
    return o
