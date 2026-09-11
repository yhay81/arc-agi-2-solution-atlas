from collections import Counter


def cp(g):
    return [row[:] for row in g]


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


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
    h, w = (len(g), len(g[0]))
    for obj in components(g, 0, True, False):
        counts = Counter((g[r][c] for r, c in obj))
        if len(counts) < 2:
            continue
        main = counts.most_common(1)[0][0]
        walls = {(r, c) for r, c in obj if g[r][c] == main}
        cargo = [p for p in obj if g[p[0]][p[1]] != main]
        colors = {g[r][c] for r, c in cargo}
        if len(colors) != 1:
            raise ValueError("Ambiguous payload")
        openings = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            clear = 0
            for r, c in cargo:
                r += dr
                c += dc
                while 0 <= r < h and 0 <= c < w and ((r, c) not in walls):
                    r += dr
                    c += dc
                clear += not (0 <= r < h and 0 <= c < w)
            if clear == len(cargo):
                openings.append((dr, dc))
        if len(openings) != 1:
            raise ValueError("No unique open side")
        dr, dc = (-openings[0][0], -openings[0][1])
        extent = max((r * dr + c * dc for r, c in walls))
        tip = [p for p in walls if p[0] * dr + p[1] * dc == extent]
        if len(tip) != 1:
            raise ValueError("No unique nozzle")
        for r, c in cargo:
            out[r][c] = 0
        r, c = tip[0]
        for k in range(1, len(cargo) + 1):
            put(out, r + dr * k, c + dc * k, next(iter(colors)))
    return out
