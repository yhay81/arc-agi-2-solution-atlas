from collections import Counter


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    bg = Counter(v for row in g for v in row).most_common(1)[0][0]
    points = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != bg]
    ph = max((r for r, c in points))
    pw = max((c for r, c in points))
    border = g[ph][pw]
    if not all(g[ph][c] == border for c in range(pw + 1)) or not all(
        g[r][pw] == border for r in range(ph + 1)
    ):
        raise ValueError("Expected top-left seed with solid bottom and right border")
    seed = [row[:pw] for row in g[:ph]]
    fg = {v for row in seed for v in row if v != bg}
    if len(fg) != 1:
        raise ValueError("Expected one seed color")
    color = next(iter(fg))
    return [
        [
            bg
            if seed[r % ph][c % pw] == bg
            else color
            if seed[r // ph % ph][c // pw % pw] != bg
            else border
            for c in range(w)
        ]
        for r in range(h)
    ]
