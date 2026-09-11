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


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    counts = Counter(v for row in g for v in row)
    background = counts.most_common(1)[0][0]
    colors = [v for v in counts if v != background]
    marker_color = next((v for v in colors if counts[v] == 5), None)
    if marker_color is None:
        raise ValueError("Five-cell marker not found")
    body_colors = [v for v in colors if v != marker_color]
    if len(body_colors) != 1:
        raise ValueError("Object color is ambiguous")
    body = body_colors[0]
    out = cp(g)
    if marker_color in (1, 8):
        for r, c in points(g, marker_color):
            out[r][c] = background
    mask = [[body if v == body else background for v in row] for row in g]
    for obj in components(mask, background, False, True):
        a, b, c, d = bbox(obj)
        height = b - a + 1
        width = d - c + 1
        if height == width and height % 2 == 1 and (len(obj) == height * width):
            out[(a + b) // 2][(c + d) // 2] = marker_color
    return out
