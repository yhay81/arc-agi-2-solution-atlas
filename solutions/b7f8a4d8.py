from collections import Counter


def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def solve(grid):
    g = grid
    g = cp(g)
    colors = Counter(v for row in g for v in row if v)
    frame = colors.most_common(1)[0][0]
    center = Counter(v for row in g for v in row if v not in (0, frame)).most_common(1)[0][0]
    out = cp(g)
    for color in set(colors) - {frame, center}:
        pts = points(g, color)
        for r in {r for r, c in pts}:
            cols = [c for rr, c in pts if rr == r]
            for c in range(min(cols), max(cols) + 1):
                if g[r][c] == 0:
                    out[r][c] = color
        for c in {c for r, c in pts}:
            rows = [r for r, cc in pts if cc == c]
            for r in range(min(rows), max(rows) + 1):
                if g[r][c] == 0:
                    out[r][c] = color
    return out
