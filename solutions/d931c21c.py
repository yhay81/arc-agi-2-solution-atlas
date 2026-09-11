def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    out = [r[:] for r in a]
    seen = set()
    for sy in range(h):
        for sx in range(w):
            if a[sy][sx] != 1 or (sy, sx) in seen:
                continue
            seen.add((sy, sx))
            q = [(sy, sx)]
            for y, x in q:
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        p = (y + dy, x + dx)
                        if 0 <= p[0] < h and 0 <= p[1] < w and a[p[0]][p[1]] == 1 and p not in seen:
                            seen.add(p)
                            q.append(p)
            mask = set(q)
            edge = {
                (y, x)
                for y in range(h)
                for x in range(w)
                if (y in (0, h - 1) or x in (0, w - 1)) and (y, x) not in mask
            }
            flood = list(edge)
            for y, x in flood:
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    p = (y + dy, x + dx)
                    if 0 <= p[0] < h and 0 <= p[1] < w and p not in mask and p not in edge:
                        edge.add(p)
                        flood.append(p)
            inside = {
                (y, x) for y in range(h) for x in range(w) if a[y][x] == 0 and (y, x) not in edge
            }
            if not inside:
                continue
            near = set()
            for y, x in q:
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        p = (y + dy, x + dx)
                        if 0 <= p[0] < h and 0 <= p[1] < w and p not in mask:
                            near.add(p)
            top = min(y for y, x in q)
            left = min(x for y, x in q)
            bot = max(y for y, x in q)
            right = max(x for y, x in q)
            for yy, xx, ys, xs in (
                (top - 1, left - 1, range(top, top + 2), range(left, left + 2)),
                (top - 1, right + 1, range(top, top + 2), range(right - 1, right + 1)),
                (bot + 1, left - 1, range(bot - 1, bot + 1), range(left, left + 2)),
                (bot + 1, right + 1, range(bot - 1, bot + 1), range(right - 1, right + 1)),
            ):
                if 0 <= yy < h and 0 <= xx < w and sum((y, x) in mask for y in ys for x in xs) == 3:
                    near.add((yy, xx))
            for y, x in near:
                if (y, x) in inside:
                    out[y][x] = 3
                elif a[y][x] == 0:
                    out[y][x] = 2
    return out
