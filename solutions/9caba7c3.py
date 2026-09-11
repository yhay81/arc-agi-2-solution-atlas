def cp(g):
    return [row[:] for row in g]


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
    out = cp(g)
    pending = set(points(g, 2))
    groups = []
    while pending:
        p = pending.pop()
        group = {p}
        queue = [p]
        for r, c in queue:
            close = {q for q in pending if max(abs(q[0] - r), abs(q[1] - c)) <= 2}
            pending -= close
            group |= close
            queue.extend(close)
        groups.append(group)
    for group in groups:
        a, b, c, d = bbox(group)
        boxes = []
        for r in range(max(0, b - 2), min(a, len(g) - 3) + 1):
            for col in range(max(0, d - 2), min(c, len(g[0]) - 3) + 1):
                cells = [g[r + dr][col + dc] for dr in range(3) for dc in range(3)]
                if all(v in (2, 5) for v in cells) and g[r + 1][col + 1] == 5:
                    boxes.append((r, col))
        if len(boxes) != 1:
            raise ValueError("Ambiguous 3x3 gray square")
        r, c = boxes[0]
        for dr in range(3):
            for dc in range(3):
                out[r + dr][c + dc] = 4 if dr == dc == 1 else 2 if g[r + dr][c + dc] == 2 else 7
    return out
