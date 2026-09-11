def bounds(points):
    rs, cs = zip(*points)
    return min(rs), min(cs), max(rs), max(cs)


def components(mask, diagonal=False):
    h, w = len(mask), len(mask[0])
    seen = set()
    out = []
    steps = [
        (dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if diagonal or abs(dr) + abs(dc) == 1
    ]
    for r in range(h):
        for c in range(w):
            if mask[r][c] and (r, c) not in seen:
                seen.add((r, c))
                q = [(r, c)]
                for y, x in q:
                    for dr, dc in steps:
                        p = (y + dr, x + dc)
                        if 0 <= p[0] < h and 0 <= p[1] < w and mask[p[0]][p[1]] and p not in seen:
                            seen.add(p)
                            q.append(p)
                out.append(q)
    return out


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = [row[:] for row in a]
    special = [(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v not in (0, 1)]
    r, c, b, d = bounds(special)
    legend = [row[c : d + 1] for row in a[r : b + 1]]
    objs = components([[v == 1 for v in row] for row in a], True)
    rows = sorted(set(bounds(p)[0] for p in objs))
    cols = sorted(set(bounds(p)[1] for p in objs))
    for ps in objs:
        r, c, b, d = bounds(ps)
        color = legend[rows.index(r)][cols.index(c)]
        if not (color):
            raise ValueError("task assumptions are not satisfied")
        for y, x in ps:
            out[y][x] = color
    return out
