from collections import Counter


def cp(g):
    return [row[:] for row in g]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


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
    background = bg(g)
    objects = components(g, background, False, False)
    legends = []
    for obj in objects:
        a, b, c, d = bbox(obj)
        if d - c == 1 and b > a and all(g[r][c] != background for r in range(a, b + 1)):
            legends.append((len({g[r][col] for r, col in obj}), a, b, c, d))
    if not legends:
        raise ValueError("No two-column legend")
    _, a, b, c, d = max(legends)
    mapping = [(g[r][c], g[r][d]) for r in range(a, b + 1)]
    out = cp(g)
    for color, fill in reversed(mapping):
        if fill == 0:
            fill = background
        ps = [
            (r, col)
            for r, row in enumerate(g)
            for col, v in enumerate(row)
            if v == color and (not (a <= r <= b and c <= col <= d))
        ]
        if not ps:
            continue
        top, bottom, left, right = bbox(ps)
        for r in range(top, bottom + 1):
            for col in range(left, right + 1):
                out[r][col] = fill
        for r, col in ps:
            out[r][col] = color if len(ps) != 4 or bottom - top != 1 or right - left != 1 else fill
    return out
