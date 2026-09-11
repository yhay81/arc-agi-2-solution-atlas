from collections import Counter


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    background = bg(g)
    ps = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != background}
    neighbors = lambda p: [
        (p[0] + dr, p[1] + dc)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
        if (p[0] + dr, p[1] + dc) in ps
    ]
    endpoints = [p for p in ps if len(neighbors(p)) == 1]
    current = min(endpoints)
    seen = set()
    out = []
    while current is not None:
        r, c = current
        out.append([g[r][c]])
        seen.add(current)
        nxt = [p for p in neighbors(current) if p not in seen]
        if len(nxt) > 1:
            raise ValueError("polyline branches")
        current = nxt[0] if nxt else None
    if seen != ps:
        raise ValueError("cannot traverse all cells as a single path")
    return out
