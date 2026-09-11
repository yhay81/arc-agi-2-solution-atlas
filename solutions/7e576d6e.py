from collections import Counter


def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    counts = Counter(sum(g, []))
    pathcolor = next((v for v, n in counts.items() if n == 2))
    background = bg(g)
    h, w = (len(g), len(g[0]))
    vertical = [c for c in range(w) if sum(g[r][c] != background for r in range(h)) >= h * 0.9]
    if not vertical:
        transposed = [list(row) for row in zip(*g)]
        return [list(row) for row in zip(*solve(transposed))]
    out = cp(g)
    start, end = sorted(points(g, pathcolor), key=lambda p: p[1])
    r, c = start

    def line(r1, c1, r2, c2):
        if r1 != r2 and c1 != c2:
            raise ValueError("Axis-aligned path expected")
        for rr in range(min(r1, r2), max(r1, r2) + 1):
            for cc in range(min(c1, c2), max(c1, c2) + 1):
                out[rr][cc] = pathcolor

    for wall in vertical:
        if not c < wall < end[1]:
            continue
        column = [g[rr][wall] for rr in range(h)]
        wallcolor = Counter(column).most_common(1)[0][0]
        gate = [rr for rr, v in enumerate(column) if v != wallcolor]
        center = (min(gate) + max(gate)) // 2
        line(r, c, r, wall - 1)
        line(r, wall - 1, center, wall - 1)
        r, c = (center, wall - 1)
    line(r, c, r, end[1])
    line(r, end[1], end[0], end[1])
    return out
