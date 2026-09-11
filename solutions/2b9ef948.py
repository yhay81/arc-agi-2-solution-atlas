def solve(grid):
    a = grid
    a = [row[:] for row in a]
    h, w = len(a), len(a[0])
    centers = []
    for r in range(1, len(a) - 1):
        for c in range(1, w - 1):
            if all(
                a[r + dy][c + dx] == 4
                for dy in (-1, 0, 1)
                for dx in (-1, 0, 1)
                if (dy, dx) != (0, 0)
            ) and a[r][c] not in (0, 4):
                centers.append((r, c))
    if not (len(centers) == 1):
        raise ValueError("task assumptions are not satisfied")
    cy, cx = centers[0]
    bg = a[cy][cx]
    starts = [
        (r, c)
        for r, row in enumerate(a)
        for c, v in enumerate(row)
        if v == bg and (r, c) != (cy, cx)
    ]
    if not (len(starts) == 1):
        raise ValueError("task assumptions are not satisfied")
    ends = [
        (r, c)
        for r, row in enumerate(a)
        for c, v in enumerate(row)
        if v == 4 and max(abs(r - cy), abs(c - cx)) > 1
    ]
    if not (len(ends) == 1):
        raise ValueError("task assumptions are not satisfied")
    cy += ends[0][0] - starts[0][0]
    cx += ends[0][1] - starts[0][1]
    out = [[bg] * w for _ in range(h)]
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == dx == 0:
                continue
            y, x = (cy + dy, cx + dx)
            if 0 <= y < h and 0 <= x < w:
                out[y][x] = 4
    for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        for n in range(1, max(h, w)):
            y, x = (cy + dy * n, cx + dx * n)
            if 0 <= y < h and 0 <= x < w:
                out[y][x] = 4
    return out
