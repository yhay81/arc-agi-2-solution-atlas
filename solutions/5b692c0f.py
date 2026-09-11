from collections import Counter


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
    objects = components(g, 0, True, False)
    out = [[0] * len(g[0]) for _ in g]
    for obj in objects:
        yellows = [(r, c) for r, c in obj if g[r][c] == 4]
        row_counts = Counter((r for r, c in yellows))
        col_counts = Counter((c for r, c in yellows))
        horizontal = max(row_counts.values()) > max(col_counts.values())
        axis = (row_counts if horizontal else col_counts).most_common(1)[0][0]
        off = [(r, c) for r, c in yellows if (r if horizontal else c) != axis]
        if len(off) != 1:
            raise ValueError("One side marker expected")
        sign = 1 if (off[0][0] if horizontal else off[0][1]) > axis else -1
        for r, c in obj:
            if ((r if horizontal else c) - axis) * sign < 0:
                continue
            put(out, r, c, g[r][c])
            rr, cc = (2 * axis - r, c) if horizontal else (r, 2 * axis - c)
            put(out, rr, cc, g[r][c])
    return out
