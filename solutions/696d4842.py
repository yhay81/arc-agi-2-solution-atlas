def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    unseen = {(r, c) for r in range(h) for c in range(w) if a[r][c]}
    objs = []
    while unseen:
        stack = [unseen.pop()]
        p = []
        while stack:
            q = stack.pop()
            p.append(q)
            for n in ((q[0] - 1, q[1]), (q[0] + 1, q[1]), (q[0], q[1] - 1), (q[0], q[1] + 1)):
                if n in unseen:
                    unseen.remove(n)
                    stack.append(n)
        objs.append(p)
    dots = [p[0] for p in objs if len(p) == 1]
    out = [r[:] for r in a]
    for cells in objs:
        if len(cells) == 1:
            continue
        s = set(cells)
        ends = [
            p
            for p in s
            if sum((p[0] + dy, p[1] + dx) in s for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)))
            == 1
        ]
        candidates = []
        for head in ends:
            nb = next(p for p in s if abs(p[0] - head[0]) + abs(p[1] - head[1]) == 1)
            dy, dx = head[0] - nb[0], head[1] - nb[1]
            for dot in dots:
                dr, dc = dot[0] - head[0], dot[1] - head[1]
                if (dx == 0 and dc == 0 and dr * dy > 0) or (dy == 0 and dr == 0 and dc * dx > 0):
                    candidates.append((abs(dr) + abs(dc), head, dot, dy, dx))
        distance, head, dot, dy, dx = min(candidates)
        tail = next(p for p in ends if p != head)
        path = [tail]
        while path[-1] != head:
            q = path[-1]
            path.append(
                next(p for p in s if p not in path and abs(p[0] - q[0]) + abs(p[1] - q[1]) == 1)
            )
        for r, c in path[: distance - 1]:
            out[r][c] = a[dot[0]][dot[1]]
        for n in range(1, distance):
            out[head[0] + n * dy][head[1] + n * dx] = a[head[0]][head[1]]
    return out
