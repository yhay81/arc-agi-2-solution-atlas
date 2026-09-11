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


def components(g, background=0, diagonal=False, mono=True):
    unseen = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != background}
    out = []
    while unseen:
        p = min(unseen)
        unseen.remove(p)
        q = [p]
        cells = []
        for r, c in q:
            cells.append((r, c))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if not (dr or dc) or (not diagonal and dr and dc):
                        continue
                    n = (r + dr, c + dc)
                    if n in unseen and (not mono or g[n[0]][n[1]] == g[r][c]):
                        unseen.remove(n)
                        q.append(n)
        out.append(cells)
    return out


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = cp(g)
    background = bg(g)
    ga, gb, gc, gd = bbox(points(g, 5))
    objects = components([[1 if v == 0 else 0 for v in row] for row in g], 0, False, True)
    candidates = []
    for obj in objects:
        points_set = set(obj)
        a, b, c, d = bbox(obj)
        rectangles = []
        for top in range(a, b + 1):
            for bottom in range(top, b + 1):
                for left in range(c, d + 1):
                    for right in range(left, d + 1):
                        if all(
                            (r, col) in points_set
                            for r in range(top, bottom + 1)
                            for col in range(left, right + 1)
                        ):
                            rectangles.append(
                                ((bottom - top + 1) * (right - left + 1), top, bottom, left, right)
                            )
        _, a, b, c, d = max(rectangles)
        if max(a, ga) <= min(b, gb) and (d < gc or c > gd) and ((b - a + 1) * (d - c + 1) > 1):
            candidates.append((min(abs(d - gc), abs(c - gd)), obj, (a, b, c, d)))
    if not candidates:
        raise ValueError("No black body faces gray object")
    _, obj, (a, b, c, d) = min(candidates, key=lambda x: x[0])
    for r, col in obj:
        if not (a <= r <= b and c <= col <= d):
            out[r][col] = background
    side = d if d < gc else c
    for r in range(a, b + 1):
        out[r][side] = 6
    return out
