from collections import Counter


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
    g = [row[:] for row in g]
    background = bg(g)
    out = [[background] * len(g[0]) for _ in g]
    for obj in components(g, background, True, True):
        if len(obj) == 1:
            continue
        a, b, c, d = bbox(obj)
        s = {(r - a, col - c) for r, col in obj}
        h, w = (b - a + 1, d - c + 1)
        horizontal = {(h - 1 - r, col) for r, col in s} == s
        vertical = {(r, w - 1 - col) for r, col in s} == s
        diagonal = h == w and (
            {(col, r) for r, col in s} == s or {(w - 1 - col, h - 1 - r) for r, col in s} == s
        )
        if horizontal:
            color = 1
        elif vertical:
            color = 3
        elif diagonal:
            color = 6
        else:
            raise ValueError("No reflection symmetry")
        for r, col in obj:
            out[r][col] = color
    return out
