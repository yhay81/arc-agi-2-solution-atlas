from collections import deque


def bounds(points):
    return (
        min(r for r, c in points),
        min(c for r, c in points),
        max(r for r, c in points),
        max(c for r, c in points),
    )


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    h0, w0 = len(a), len(a[0])
    r, c, b, d = bounds([(y, x) for y, row in enumerate(a) for x, v in enumerate(row) if v == 0])
    h, w = (b - r + 1, d - c + 1)
    allowed = [[v in (0, 1, 2) for v in row] for row in a]
    start = (r, c)
    queue = deque([start])
    dist = {start: 0}
    while queue:
        y, x = queue.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            yy, xx = (y + dy, x + dx)
            if (
                0 <= yy <= len(a) - h
                and 0 <= xx <= w0 - w
                and ((yy, xx) not in dist)
                and all(allowed[rr][cc] for rr in range(yy, yy + h) for cc in range(xx, xx + w))
            ):
                dist[yy, xx] = dist[y, x] + 1
                queue.append((yy, xx))
    goals = [(yy, xx) for yy, row in enumerate(a) for xx, v in enumerate(row) if v == 2]
    goal = (sum(y for y, x in goals) / len(goals), sum(x for y, x in goals) / len(goals))

    def score(pos):
        y, x = pos
        goal_overlap = sum(a[yy][xx] == 2 for yy in range(y, y + h) for xx in range(x, x + w))
        return (
            goal_overlap,
            dist[pos],
            -((y + (h - 1) / 2 - goal[0]) ** 2 + (x + (w - 1) / 2 - goal[1]) ** 2),
        )

    y, x = max(dist, key=score)
    out = [row[:] for row in a]
    for yy in range(h0):
        for xx in range(w0):
            if out[yy][xx] == 0:
                out[yy][xx] = 1
    for yy in range(y, y + h):
        for xx in range(x, x + w):
            out[yy][xx] = 0
    return out
