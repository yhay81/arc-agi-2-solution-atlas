def solve(grid):
    a = [list(map(int, row)) for row in grid]
    h, w = len(a), len(a[0]) if a else 0
    if not h or not w:
        return a
    colors = {v for row in a for v in row}
    bg = max(colors, key=lambda c: sum(v == c for row in a for v in row))

    def components(color):
        seen, found = set(), []
        for r in range(h):
            for c in range(w):
                if a[r][c] != color or (r, c) in seen:
                    continue
                stack, part = [(r, c)], []
                seen.add((r, c))
                while stack:
                    y, x = stack.pop()
                    part.append((y, x))
                    for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                        if (
                            0 <= ny < h
                            and 0 <= nx < w
                            and a[ny][nx] == color
                            and (ny, nx) not in seen
                        ):
                            seen.add((ny, nx))
                            stack.append((ny, nx))
                found.append(part)
        return found

    candidates = [(len(components(color)), color) for color in colors - {bg}]
    if not candidates:
        return a
    color = max(candidates)[1]
    out = [row[:] for row in a]
    for comp in components(color):
        ys, xs = zip(*comp)
        top, bottom, left, right = min(ys), max(ys), min(xs), max(xs)
        block = [row[left : right + 1] for row in a[top : bottom + 1]]
        bh, bw = len(block), len(block[0])
        for y, x in comp:
            out[y][x] = bg
        if top == 0 and left == 0:
            ny, nx = bh, bw
        elif top == 0 and right == w - 1:
            ny, nx = bh, w - 2 * bw
        elif bottom == h - 1 and left == 0:
            ny, nx = h - 2 * bh, bw
        elif bottom == h - 1 and right == w - 1:
            ny, nx = h - 2 * bh, w - 2 * bw
        else:
            continue
        if ny < 0 or nx < 0 or ny + bh > h or nx + bw > w:
            continue
        for dy in range(bh):
            for dx in range(bw):
                out[ny + dy][nx + dx] = block[dy][dx]
    return out
