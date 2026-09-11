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
    g = [row[:] for row in g]
    out = cp(g)
    objs = components([[2 if v == 2 else 0 for v in row] for row in g], 0, False, True)
    h, w = (len(g), len(g[0]))
    red_boxes = [bbox(o) for o in objs]
    for o in objs:
        a, b, c, d = bbox(o)
        corners = [(a - 1, c - 1), (a - 1, d + 1), (b + 1, d + 1), (b + 1, c - 1)]
        values = [g[r][col] for r, col in corners]
        for i, (r, col) in enumerate(corners):
            color = values[(i - 1) % 4]
            dr = -1 if i < 2 else 1
            dc = 1 if i in (1, 2) else -1
            while 0 <= r < h and 0 <= col < w:
                if g[r][col] == 2:
                    break
                out[r][col] = color
                absorbed = False
                for aa, bb, cc, dd in red_boxes:
                    if any(
                        (
                            (r + rr, col + dc2)
                            in {
                                (rrr, ccc) for rrr in range(aa, bb + 1) for ccc in range(cc, dd + 1)
                            }
                            for rr, dc2 in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                        )
                    ):
                        pr, pc = (bb + 1, cc - 1)
                        if dr == 1 and 0 <= pr < h and (0 <= pc < w) and (g[pr][pc] == color):
                            absorbed = True
                            break
                if absorbed:
                    break
                r += dr
                col += dc
    return out
