from collections import Counter


def mode(values):
    return Counter(values).most_common(1)[0][0]


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


def bounds(points):
    rs, cs = zip(*points)
    return min(rs), min(cs), max(rs), max(cs)


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    bg = mode([v for row in a for v in row])
    objs = components([[v != bg for v in row] for row in a], True)
    parts = []
    for ps in objs:
        r, c, b, d = bounds(ps)
        parts.append([row[c : d + 1] for row in a[r : b + 1]])
    if not (all(len(p) == len(parts[0]) and len(p[0]) == len(parts[0][0]) for p in parts)):
        raise ValueError("task assumptions are not satisfied")
    out = [[0] * len(parts[0][0]) for _ in parts[0]]
    for p in parts:
        for r, row in enumerate(p):
            for c, v in enumerate(row):
                if v:
                    out[r][c] = v
    return out
