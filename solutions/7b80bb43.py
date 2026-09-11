from collections import Counter


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    background = bg(g)
    color = next(v for v in sum(g, []) if v != background)
    h, w = (len(g), len(g[0]))
    ps = set(points(g, color))
    base = {
        p
        for p in ps
        if any(((p[0] + dr, p[1] + dc) in ps for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]))
    }
    bent = {
        p
        for p in ps - base
        if any((p[0] + dr, p[1] + dc) in ps for dr in (-1, 1) for dc in (-1, 1))
    }
    keep = ps - bent
    rows = {r for r in range(h) if sum((r, c) in base for c in range(w)) >= 4}
    cols = {c for c in range(w) if sum((r, c) in base for r in range(h)) >= 4}
    bent |= {
        p
        for p in keep
        if p[0] not in rows
        and p[1] not in cols
        and any((p[0] + dr, p[1] + dc) in bent for dr in (-1, 1) for dc in (-1, 1))
    }
    keep = ps - bent
    out = [[color if (r, c) in keep else background for c in range(w)] for r in range(h)]
    for vertical, lines, n in [(False, rows, w), (True, cols, h)]:
        for line in lines:
            anchors = [p for p in range(n) if ((p, line) if vertical else (line, p)) in keep]
            for a, b in zip(anchors, anchors[1:]):
                if b - a <= 1:
                    continue
                attached = False
                for p, sign in [(a, 1), (b, -1)]:
                    for q in [-1, 1]:
                        r, c = (p + sign, line + q) if vertical else (line + q, p + sign)
                        if (r, c) in bent:
                            attached = True
                if attached:
                    for p in range(a + 1, b):
                        if vertical:
                            out[p][line] = color
                        else:
                            out[line][p] = color
    return out
