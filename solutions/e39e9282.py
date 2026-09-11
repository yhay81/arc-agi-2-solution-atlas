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
    blocks = components([[v if v in (5, 6) else 8 for v in row] for row in g], 8, False, True)
    out = cp(g)
    moves = []
    for o in blocks:
        a, b, c, d = bbox(o)
        gray = g[o[0][0]][o[0][1]] == 5
        for r, col in points(g, 9):
            if a <= r <= b and col in (c - 1, d + 1):
                moves.append((r, col, r, col + (1 if col < c else -1) * (1 if gray else 2), gray))
            elif c <= col <= d and r in (a - 1, b + 1):
                moves.append((r, col, r + (1 if r < a else -1) * (1 if gray else 2), col, gray))
        if gray:
            for r, col in o:
                out[r][col] = 8
    for r, c, a, b, gray in moves:
        if not gray:
            out[r][c] = 8
    for r, c, a, b, gray in moves:
        out[a][b] = 9
    return out
