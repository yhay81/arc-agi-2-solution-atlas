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
    gray = max(
        components([[5 if v == 5 else 0 for v in row] for row in g], 0, False, True), key=len
    )
    a, b, c, d = bbox(gray)
    marks = [
        (r, col, g[r][col])
        for r in range(a, b + 1)
        for col in range(c, d + 1)
        if g[r][col] not in (0, 5)
    ]
    if len(marks) != 1:
        raise ValueError("Expected one instruction in gray corner")
    r, c, color = marks[0]
    out = [[0 if v == color else v for v in row] for row in g]
    out[r][c] = color
    return out
