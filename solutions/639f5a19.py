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
                part = []
                for y, x in q:
                    part.append((y, x))
                    for dr, dc in steps:
                        p = (y + dr, x + dc)
                        if 0 <= p[0] < h and 0 <= p[1] < w and mask[p[0]][p[1]] and p not in seen:
                            seen.add(p)
                            q.append(p)
                out.append(part)
    return out


def bounds(points):
    rs, cs = zip(*points)
    return (min(rs), min(cs), max(rs), max(cs))


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = [row[:] for row in a]
    for ps in components([[v == 8 for v in row] for row in a]):
        r, c, b, d = bounds(ps)
        h, w = (b - r + 1, d - c + 1)
        for y, x in ps:
            yy, xx = (y - r, x - c)
            out[y][x] = (
                4
                if min(yy, xx, h - 1 - yy, w - 1 - xx) >= 2
                else ((6, 1), (2, 3))[int(yy >= h / 2)][int(xx >= w / 2)]
            )
    return out
