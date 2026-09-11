from collections import Counter


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
    pending = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v}
    groups = []
    while pending:
        p = pending.pop()
        obj = {p}
        queue = [p]
        for r, c in queue:
            near = {q for q in pending if max(abs(q[0] - r), abs(q[1] - c)) <= 2}
            pending -= near
            obj |= near
            queue.extend(near)
        groups.append(obj)
    main = max(groups, key=len)
    a, b, c, d = bbox(main)
    n = b - a + 1
    if n != d - c + 1:
        raise ValueError("Main pattern is not square")
    counts = Counter((g[r][col] for obj in groups if obj is not main for r, col in obj))
    out = [[0] * n for _ in range(n)]
    for r, col in main:
        v = g[r][col]
        rr, cc = (r - a, col - c)
        for _ in range(counts[v] % 4):
            rr, cc = (cc, n - 1 - rr)
        if out[rr][cc] not in (0, v):
            raise ValueError("Rotated layers overlap")
        out[rr][cc] = v
    return out
