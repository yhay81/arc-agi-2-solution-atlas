def bounds(points):
    return (
        min(r for r, _ in points),
        min(c for _, c in points),
        max(r for r, _ in points),
        max(c for _, c in points),
    )


def components(grid, color):
    h, w = len(grid), len(grid[0])
    seen = set()
    result = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != color or (r, c) in seen:
                continue
            seen.add((r, c))
            stack = [(r, c)]
            part = []
            while stack:
                x, y = stack.pop()
                part.append((x, y))
                for p in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if (
                        0 <= p[0] < h
                        and 0 <= p[1] < w
                        and grid[p[0]][p[1]] == color
                        and p not in seen
                    ):
                        seen.add(p)
                        stack.append(p)
            result.append(part)
    return result


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = [row[:] for row in a]
    palette = [v for row in a for v in row if v not in (0, 5)]
    for ps in components(a, 5):
        r, c, b, d = bounds(ps)
        mr = sum(y for y, _ in ps) / len(ps)
        mc = sum(x for _, x in ps) / len(ps)
        positive = sum((y - mr) * (x - mc) for y, x in ps) >= 0
        tip = sum(v == 5 for v in a[r][c : d + 1])
        last = min(b - r + 1, d - c + 1) - tip
        for y, x in ps:
            out[y][x] = palette[min(y - r, x - c if positive else d - x, last) % len(palette)]
    return out
