from collections import Counter


def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    background = bg(g)
    color = next(v for v in sum(g, []) if v != background)
    boundary = (
        [(0, c) for c in range(w)]
        + [(r, w - 1) for r in range(1, h)]
        + [(h - 1, c) for c in range(w - 2, -1, -1)]
        + [(r, 0) for r in range(h - 2, 0, -1)]
    )
    n = len(points(g, color))
    marks = [i for i, (r, c) in enumerate(boundary) if g[r][c] == color]
    out = cp(g)
    phases = [p for p in range(2 * n) if all((i - p) % (2 * n) < n for i in marks)]
    if len(phases) != 1:
        raise ValueError("Ambiguous perimeter phase")
    for i, (r, c) in enumerate(boundary):
        out[r][c] = color if (i - phases[0]) % (2 * n) < n else background
    return out
