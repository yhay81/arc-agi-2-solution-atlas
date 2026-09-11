from collections import Counter


def mode(values):
    return Counter(values).most_common(1)[0][0]


def bounds(points):
    rs, cs = zip(*points)
    return min(rs), min(cs), max(rs), max(cs)


def components(mask, diagonal=False):
    h, w = len(mask), len(mask[0])
    seen = set()
    res = []
    for r in range(h):
        for c in range(w):
            if mask[r][c] and (r, c) not in seen:
                seen.add((r, c))
                q = [(r, c)]
                for y, x in q:
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        p = (y + dy, x + dx)
                        if 0 <= p[0] < h and 0 <= p[1] < w and mask[p[0]][p[1]] and p not in seen:
                            seen.add(p)
                            q.append(p)
                res.append(q)
    return res


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    bg = mode([v for row in a for v in row])
    out = [row[:] for row in a]
    candidates = []
    for ps in components([[v != bg for v in row] for row in a]):
        r, c, b, d = bounds(ps)
        if (
            d - c == 1
            and b - r >= 1
            and all(a[y][x] != bg for y in range(r, b + 1) for x in range(c, d + 1))
        ):
            candidates.append((b - r, r, c, b, d))
    _, r, c, b, d = max(candidates)
    table = [row[c : d + 1] for row in a[r : b + 1]]
    mask = [[v != bg for v in row] for row in a]
    for y in range(r, b + 1):
        for x in range(c, d + 1):
            mask[y][x] = False
    for left, right in table:
        for y in range(len(a)):
            for x in range(len(a[0])):
                if mask[y][x] and out[y][x] == left:
                    out[y][x] = right
    return out
