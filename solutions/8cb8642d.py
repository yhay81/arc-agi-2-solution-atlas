from collections import Counter


def mode(values):
    return Counter(values).most_common(1)[0][0]


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
    out = [row[:] for row in a]
    for ps in components([[v != 0 for v in row] for row in a]):
        r, c, b, d = bounds(ps)
        p = [row[c : d + 1] for row in a[r : b + 1]]
        base = mode(p[0])
        inner = mode([v for row in p for v in row if v not in (base, 0)])
        for y in range(r + 1, b):
            for x in range(c + 1, d):
                out[y][x] = 0
        h = b - r - 1
        w = d - c - 1
        for y in range(h):
            for x in range(w):
                dy = min(y, h - 1 - y)
                dx = min(x, w - 1 - x)
                if (
                    dy == dx
                    or (h < w and dy == (h - 1) // 2 and (dx > dy))
                    or (w < h and dx == (w - 1) // 2 and (dy > dx))
                ):
                    out[r + y + 1][c + x + 1] = inner
    return out
