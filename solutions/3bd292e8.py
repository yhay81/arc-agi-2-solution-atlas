def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    red = set(points(g, 2))
    seen = set()
    redcomps = []
    for start in sorted(red):
        if start in seen:
            continue
        q = [start]
        seen.add(start)
        obj = []
        while q:
            p = q.pop()
            obj.append(p)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                z = (p[0] + dr, p[1] + dc)
                if z in red and z not in seen:
                    seen.add(z)
                    q.append(z)
        redcomps.append(obj)
    labels = {}
    regions = []
    for r in range(h):
        for c in range(w):
            if g[r][c] != 7 or (r, c) in labels:
                continue
            idx = len(regions)
            q = [(r, c)]
            labels[r, c] = idx
            obj = []
            while q:
                p = q.pop()
                obj.append(p)
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    z = (p[0] + dr, p[1] + dc)
                    if (
                        0 <= z[0] < h
                        and 0 <= z[1] < w
                        and (g[z[0]][z[1]] == 7)
                        and (z not in labels)
                    ):
                        labels[z] = idx
                        q.append(z)
            regions.append(obj)
    graph = [set() for _ in regions]
    for r, c in red:
        for (a, b), (x, y) in (((r - 1, c), (r + 1, c)), ((r, c - 1), (r, c + 1))):
            if (a, b) in labels and (x, y) in labels and (labels[a, b] != labels[x, y]):
                u, v = (labels[a, b], labels[x, y])
                graph[u].add(v)
                graph[v].add(u)
    choices = []
    for obj in redcomps:
        ends = [
            p
            for p in obj
            if sum(((p[0] + dr, p[1] + dc) in red for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))))
            == 1
        ]
        for p in ends:
            if p[0] == 0:
                choices.append((0, p[1], p, obj))
            elif p[1] == 0:
                choices.append((1, p[0], p, obj))
    if not choices:
        raise ValueError("No entering red path")
    _, _, start, path = min(choices, key=lambda x: (x[0], x[1]))
    pathset = set(path)
    prev = None
    cur = start
    seed = None
    while True:
        nxt = [
            (cur[0] + dr, cur[1] + dc)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
            if (cur[0] + dr, cur[1] + dc) in pathset and (cur[0] + dr, cur[1] + dc) != prev
        ]
        if not nxt:
            break
        new = nxt[0]
        dr, dc = (new[0] - cur[0], new[1] - cur[1])
        left = (cur[0] - dc, cur[1] + dr)
        if left in labels:
            seed = labels[left]
            break
        prev, cur = (cur, new)
    if seed is None:
        raise ValueError("Cannot identify left-side region")
    colors = {seed: 3 if len(path) % 2 else 5}
    q = [seed]
    while q:
        u = q.pop(0)
        for v in graph[u]:
            if v not in colors:
                colors[v] = 8 - colors[u]
                q.append(v)
    out = cp(g)
    for idx, obj in enumerate(regions):
        if idx not in colors:
            raise ValueError("Disconnected region graph")
        for r, c in obj:
            out[r][c] = colors[idx]
    return out
