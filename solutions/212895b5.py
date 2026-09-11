def components(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    out = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 5 or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            part = []
            while stack:
                y, x = stack.pop()
                part.append((y, x))
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        q = (y + dy, x + dx)
                        if (
                            0 <= q[0] < h
                            and 0 <= q[1] < w
                            and grid[q[0]][q[1]] == 5
                            and q not in seen
                        ):
                            seen.add(q)
                            stack.append(q)
            out.append(part)
    return out


def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    a = [r[:] for r in a]
    blocked = [[v == 5 for v in row] for row in a]
    for ps in components(a):
        for y in {r for r, c in ps}:
            cols = sorted(c for r, c in ps if r == y)
            for l, r in zip(cols, cols[1:]):
                if r - l == 2:
                    blocked[y][l + 1] = True
        for x in {c for r, c in ps}:
            rows = sorted(r for r, c in ps if c == x)
            for t, b in zip(rows, rows[1:]):
                if b - t == 2:
                    blocked[t + 1][x] = True
    cells = [(r, c) for r in range(h) for c in range(w) if a[r][c] == 8]
    r = min(y for y, x in cells)
    c = min(x for y, x in cells)
    b = max(y for y, x in cells)
    d = max(x for y, x in cells)
    out = [x[:] for x in a]
    for y, x, dy, dx in [(r, c, -1, -1), (r, d, -1, 1), (b, c, 1, -1), (b, d, 1, 1)]:
        while True:
            y += dy
            x += dx
            if not (0 <= y < h and 0 <= x < w) or blocked[y][x]:
                break
            out[y][x] = 2
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    starts = [(r, (c + d) // 2), ((r + b) // 2, d), (b, (c + d) // 2), ((r + b) // 2, c)]
    for i, (y, x) in enumerate(starts):
        for step in range(2 * (h + w)):
            dy, dx = dirs[(i + (step // 2) % 2) % 4]
            y += dy
            x += dx
            if not (0 <= y < h and 0 <= x < w) or a[y][x] == 5:
                break
            out[y][x] = 4
    return out
