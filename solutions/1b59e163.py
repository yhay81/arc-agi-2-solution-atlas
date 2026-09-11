from collections import Counter


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


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
    background = bg(g)
    objects = components(
        [[background if v == 5 else v for v in row] for row in g], background, True, False
    )
    templates = {}
    markers = []
    out = [[background] * len(g[0]) for row in g]
    for obj in objects:
        if len(obj) == 1:
            markers += obj
            continue
        counts = Counter((g[r][c] for r, c in obj))
        anchors = [color for color, n in counts.items() if n == 1]
        if len(anchors) != 1:
            raise ValueError("Unique anchor expected")
        color = anchors[0]
        ar, ac = next(((r, c) for r, c in obj if g[r][c] == color))
        templates[color] = [(r - ar, c - ac, g[r][c]) for r, c in obj]
    for r, c in markers:
        color = g[r][c]
        if color not in templates:
            raise ValueError("No matching template")
        for dr, dc, v in templates[color]:
            put(out, r + dr, c + dc, v)
    return out
