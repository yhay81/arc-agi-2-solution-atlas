def bounds(points):
    return (
        min(r for r, _ in points),
        min(c for _, c in points),
        max(r for r, _ in points),
        max(c for _, c in points),
    )


def components(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    out = []
    for r in range(h):
        for c in range(w):
            if not grid[r][c] or (r, c) in seen:
                continue
            seen.add((r, c))
            stack = [(r, c)]
            part = []
            while stack:
                x, y = stack.pop()
                part.append((x, y))
                for p in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= p[0] < h and 0 <= p[1] < w and grid[p[0]][p[1]] and p not in seen:
                        seen.add(p)
                        stack.append(p)
            out.append(part)
    return out


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    objs = components([[v != 8 for v in row] for row in a])
    source = next(ps for ps in objs if any(a[r][c] == 4 for r, c in ps))
    target = next(ps for ps in objs if not any(a[r][c] == 4 for r, c in ps))
    sr, sc, sb, sd = bounds(source)
    tr, tc, tb, td = bounds(target)
    marker = next(v for r, c in source if (v := a[r][c]) not in (0, 4))
    p = next((r, c) for r in range(sr, sb + 1) for c in range(sc, sd + 1) if a[r][c] == marker)
    q = next((r, c) for r in range(tr, tb + 1) for c in range(tc, td + 1) if a[r][c] == marker)
    out = [row[tc : td + 1] for row in a[tr : tb + 1]]
    for y, row in enumerate(a):
        for x, v in enumerate(row):
            if v == 4:
                yy, xx = y + q[0] - p[0] - tr, x + q[1] - p[1] - tc
                if 0 <= yy < len(out) and 0 <= xx < len(out[0]):
                    out[yy][xx] = 4
    return out
