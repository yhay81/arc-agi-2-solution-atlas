def solve(grid):
    a = [list(map(int, row)) for row in grid]
    h, w = len(a), len(a[0]) if a else 0
    if not h or not w:
        return a
    colors = {v for row in a for v in row}
    bg = max(colors, key=lambda c: sum(v == c for row in a for v in row))
    out = [row[:] for row in a]
    for c in range(w):
        rows = [r for r in range(h) if a[r][c] == 9]
        if rows:
            for r in range(rows[0], h):
                if a[r][c] == bg:
                    out[r][c] = 1
    seen = set()
    for r in range(h):
        for c in range(w):
            if a[r][c] != 9 or (r, c) in seen:
                continue
            stack, comp = [(r, c)], []
            seen.add((r, c))
            while stack:
                y, x = stack.pop()
                comp.append((y, x))
                for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                    if 0 <= ny < h and 0 <= nx < w and a[ny][nx] == 9 and (ny, nx) not in seen:
                        seen.add((ny, nx))
                        stack.append((ny, nx))
            ys, xs = zip(*comp)
            top, bottom, left, right = min(ys), max(ys), min(xs), max(xs)
            t = (right - left + 1) // 2
            for y in range(top - t, bottom + t + 1):
                for x in range(left - t, right + t + 1):
                    if (
                        0 <= y < h
                        and 0 <= x < w
                        and not (top <= y <= bottom and left <= x <= right)
                        and a[y][x] == bg
                    ):
                        out[y][x] = 3
    return out
