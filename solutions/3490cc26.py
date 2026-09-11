def components(a):
    h, w = len(a), len(a[0])
    unseen = {(r, c) for r in range(h) for c in range(w) if a[r][c]}
    out = []
    while unseen:
        stack = [unseen.pop()]
        group = []
        while stack:
            p = stack.pop()
            group.append(p)
            for q in ((p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)):
                if q in unseen:
                    unseen.remove(q)
                    stack.append(q)
        out.append(group)
    return out


def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    objs = components(a)
    rects = [
        (min(r for r, c in p), min(c for r, c in p), max(r for r, c in p), max(c for r, c in p))
        for p in objs
    ]
    start = next(i for i, p in enumerate(objs) if a[p[0][0]][p[0][1]] == 2)
    neighbors = {i: [] for i in range(len(objs))}
    for i, (r, c, b, d) in enumerate(rects):
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            cand = []
            for j, (y, x, z, q) in enumerate(rects):
                if i == j:
                    continue
                if dr and c == x and d == q and (y - r) * dr > 0:
                    cand.append((abs(y - r), j))
                if dc and r == y and b == z and (x - c) * dc > 0:
                    cand.append((abs(x - c), j))
            if cand:
                neighbors[i].append(min(cand))
    best = ([start], 0)

    def dfs(path, cost):
        nonlocal best
        if (len(path), -cost) > (len(best[0]), -best[1]):
            best = (path, cost)
        for dist, j in neighbors[path[-1]]:
            if j not in path:
                dfs(path + [j], cost + dist)

    dfs([start], 0)
    out = [r[:] for r in a]
    for i, j in zip(best[0], best[0][1:]):
        r, c, b, d = rects[i]
        y, x, z, q = rects[j]
        for rr in range(min(r, y), max(b, z) + 1):
            for cc in range(min(c, x), max(d, q) + 1):
                if out[rr][cc] == 0:
                    out[rr][cc] = 7
    return out
