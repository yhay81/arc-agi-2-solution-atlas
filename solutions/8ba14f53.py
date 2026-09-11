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


def crop(g, cells):
    a, b, c, d = bbox(cells)
    return [list(row[c : d + 1]) for row in g[a : b + 1]]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    objs = components(g, 0, False, True)
    objs.sort(key=lambda o: min((c for r, c in o)))
    rows = []
    for o in objs:
        a, b, c, d = bbox(o)
        patch = crop(g, o)
        outside = set()
        q = []
        for r, row in enumerate(patch):
            for col, v in enumerate(row):
                if v == 0 and (r in (0, len(patch) - 1) or col in (0, len(row) - 1)):
                    q.append((r, col))
                    outside.add((r, col))
        for r, col in q:
            for rr, cc in ((r - 1, col), (r + 1, col), (r, col - 1), (r, col + 1)):
                if (
                    0 <= rr < len(patch)
                    and 0 <= cc < len(patch[0])
                    and (patch[rr][cc] == 0)
                    and ((rr, cc) not in outside)
                ):
                    outside.add((rr, cc))
                    q.append((rr, cc))
        count = sum(
            (
                v == 0 and (r, col) not in outside
                for r, row in enumerate(patch)
                for col, v in enumerate(row)
            )
        )
        color = g[o[0][0]][o[0][1]]
        while count > 0:
            n = min(3, count)
            rows.append([color] * n + [0] * (3 - n))
            count -= n
    if len(rows) > 3:
        raise ValueError("Output overflow")
    return rows + [[0] * 3 for _ in range(3 - len(rows))]
