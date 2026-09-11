def bbox(ps):
    return (
        min((r for r, c in ps)),
        min((c for r, c in ps)),
        max((r for r, c in ps)),
        max((c for r, c in ps)),
    )


def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    vertical = sum(all(row[c] == 0 for row in g) for c in range(len(g[0])))
    horizontal = sum(all(v == 0 for v in row) for row in g)
    if vertical > horizontal:
        t = [list(row) for row in zip(*g)]
        return [list(row) for row in zip(*solve(t))]
    centers = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 6]
    top, left, bottom, right = bbox(centers)
    width = right - left + 1
    bands = []
    start = None
    for r, row in enumerate(g + [[0] * len(g[0])]):
        if any(row) and start is None:
            start = r
        if not any(row) and start is not None:
            bands.append((start, r))
            start = None
    center_index = next((i for i, (a, b) in enumerate(bands) if a <= top < b))
    out = copy(g)
    for i, (a, b) in enumerate(bands):
        if i == center_index:
            continue
        gap = (abs(i - center_index) - 1) * width
        for r in range(a, b):
            for c, v in enumerate(g[r]):
                if v == 8 and (c < left - gap or c > right + gap):
                    out[r][c] = 4
    return out
