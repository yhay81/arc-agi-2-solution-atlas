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
    h, w = (len(g), len(g[0]))
    objs = components(g, 0, False, True)
    corners = [
        o
        for o in objs
        if len(o) == 3 and bbox(o)[1] - bbox(o)[0] == 1 and (bbox(o)[3] - bbox(o)[2] == 1)
    ]
    if len(corners) != 4:
        raise ValueError("Four L corners expected")
    a, b, c, d = bbox([p for o in corners for p in o])
    colors = Counter(g[o[0][0]][o[0][1]] for o in corners)
    fill = next((color for color, n in colors.items() if n == 1))
    frame = next((color for color, n in colors.items() if n == 3))
    out = cp(g)
    for r in range(h):
        for col in range(w):
            if a <= r <= b or c <= col <= d:
                out[r][col] = fill
    for r in range(a, b + 1):
        out[r][c] = out[r][d] = frame
    for col in range(c, d + 1):
        out[a][col] = out[b][col] = frame
    for r in range(h):
        for col in range(w):
            color = g[r][col]
            if color == 0:
                continue
            if c <= col <= d and r < a:
                for rr in range(r + 1):
                    out[rr][col] = color
            elif c <= col <= d and r > b:
                for rr in range(r, h):
                    out[rr][col] = color
            elif a <= r <= b and col < c:
                for cc in range(col + 1):
                    out[r][cc] = color
            elif a <= r <= b and col > d:
                for cc in range(col, w):
                    out[r][cc] = color
    for r in range(h):
        for col in range(w):
            if g[r][col] != 0 and (not (a <= r <= b and c <= col <= d)):
                out[r][col] = g[r][col]
    return out
