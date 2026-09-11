from collections import Counter


def mode(values):
    return Counter(values).most_common(1)[0][0]


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    gray = [r for r, row in enumerate(a) if all(v == 5 for v in row)]
    if not (gray):
        raise ValueError("task assumptions are not satisfied")
    cut = max(gray) + 1
    field = [row[:] for row in a[cut:]]
    bg = mode(v for row in field for v in row)
    points = [(r, c) for r, row in enumerate(field) for c, v in enumerate(row) if v == 8]
    r, c = min(x[0] for x in points), min(x[1] for x in points)
    b, d = max(x[0] for x in points), max(x[1] for x in points)
    n = b - r + 1
    if not (n == d - c + 1):
        raise ValueError("task assumptions are not satisfied")
    turns = {}
    for start in range(0, len(a[0]), cut):
        swatch = a[1][start + 1 : start + cut - 1]
        hits = [i for i, v in enumerate(swatch) if v not in (0, 5)]
        if not (len(hits) == 1):
            raise ValueError("task assumptions are not satisfied")
        i = hits[0]
        turns[swatch[i]] = -1 if i < len(swatch) / 2 else 1
    out = [row[:] for row in field]
    h, w = len(out), len(out[0])
    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        y, x, seen = r, c, set()
        while (y, x, dy, dx) not in seen:
            seen.add((y, x, dy, dx))
            yy, xx = y + dy, x + dx
            if yy < 0 or xx < 0 or yy + n > h or xx + n > w:
                break
            obstacle = [
                out[rr][cc]
                for rr in range(yy, yy + n)
                for cc in range(xx, xx + n)
                if out[rr][cc] not in (bg, 8)
            ]
            if obstacle:
                color = obstacle[0]
                if color not in turns:
                    raise ValueError("task assumptions are not satisfied")
                dy, dx = (dx, -dy) if turns[color] == 1 else (-dx, dy)
                continue
            for rr in range(yy, yy + n):
                for cc in range(xx, xx + n):
                    out[rr][cc] = 8
            y, x = yy, xx
    return out
