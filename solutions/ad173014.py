def bounds(points):
    rs, cs = zip(*points)
    return min(rs), min(cs), max(rs), max(cs)


def components(mask, diagonal=False):
    h, w = len(mask), len(mask[0])
    seen = set()
    res = []
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
                res.append(q)
    return res


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    boxes = [bounds(p) for p in components([[v == 2 for v in row] for row in a], 4) if len(p) >= 8]
    cy = sum((b[0] + b[2]) / 2 for b in boxes) / len(boxes)
    cx = sum((b[1] + b[3]) / 2 for b in boxes) / len(boxes)
    import math

    boxes.sort(key=lambda b: math.atan2((b[0] + b[2]) / 2 - cy, (b[1] + b[3]) / 2 - cx))
    colors = []
    for y, x, v, u in boxes:
        cs = {a[yy][xx] for yy in range(y + 1, v) for xx in range(x + 1, u)} - {0, 1, 2}
        if not (len(cs) == 1):
            raise ValueError("task assumptions are not satisfied")
        colors.append(cs.pop())
    o = [row[:] for row in a]
    for i, (y, x, v, u) in enumerate(boxes):
        for yy in range(y + 1, v):
            for xx in range(x + 1, u):
                if o[yy][xx] == colors[i]:
                    o[yy][xx] = colors[(i + 1) % len(colors)]
    return o
