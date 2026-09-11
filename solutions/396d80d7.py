from collections import Counter


def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    background = bg(g)
    counts = Counter(v for row in g for v in row if v != background)
    fill = min(
        counts,
        key=lambda v: (
            (bbox(points(g, v))[1] - bbox(points(g, v))[0] + 1)
            * (bbox(points(g, v))[3] - bbox(points(g, v))[2] + 1)
        ),
    )
    shape = next(v for v in counts if v != fill)
    out = cp(g)
    for r in range(h):
        for c in range(w):
            if g[r][c] != background:
                continue
            diag = any(
                0 <= r + dr < h and 0 <= c + dc < w and (g[r + dr][c + dc] == shape)
                for dr in (-1, 1)
                for dc in (-1, 1)
            )
            side = any(
                (
                    0 <= r + dr < h and 0 <= c + dc < w and (g[r + dr][c + dc] == shape)
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
                )
            )
            if diag and (not side):
                out[r][c] = fill
    return out
