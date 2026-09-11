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
                    for dy in (-1, 0, 1):
                        for dx in (-1, 0, 1):
                            ny, nx = y + dy, x + dx
                            if (
                                (dy or dx)
                                and 0 <= ny < h
                                and 0 <= nx < w
                                and a[ny][nx] == color
                                and (ny, nx) not in seen
                            ):
                                seen.add((ny, nx))
                                stack.append((ny, nx))
                found.append(part)
        return found

    lines, others = [], []
    for color in colors - {bg}:
        for comp in components(color):
            ys, xs = zip(*comp)
            ry, rx = max(ys) - min(ys), max(xs) - min(xs)
            straight = len(comp) >= 3 and (
                (ry == 0 and len(comp) == rx + 1)
                or (rx == 0 and len(comp) == ry + 1)
                or (ry == rx and len(comp) == ry + 1)
            )
            (lines if straight else others).append((len(comp), color, comp))
    if not lines or not others:
        return a
    _, line_color, line = max(lines, key=lambda x: x[0])
    ys, xs = zip(*line)
    if len(set(ys)) == 1:
        endpoints = [(ys[0], min(xs)), (ys[0], max(xs))]
    elif len(set(xs)) == 1:
        endpoints = [(min(ys), xs[0]), (max(ys), xs[0])]
    else:
        endpoints = [min(line), max(line)]
    _, _, template_comp = max(others, key=lambda x: x[0])
    top, left = min(y for y, _ in template_comp), min(x for _, x in template_comp)
    bottom, right = max(y for y, _ in template_comp), max(x for _, x in template_comp)
    template = [row[left : right + 1] for row in a[top : bottom + 1]]
    th, tw = len(template), len(template[0])
    out = [[bg] * w for _ in range(h)]
    for ey, ex in endpoints:
        sy, sx = ey - (th - 1) // 2, ex - (tw - 1) // 2
        for y in range(th):
            for x in range(tw):
                if template[y][x] != bg and 0 <= sy + y < h and 0 <= sx + x < w:
                    out[sy + y][sx + x] = template[y][x]
    centers = [
        (
            (min(y for y, _ in c) + max(y for y, _ in c)) // 2,
            (min(x for _, x in c) + max(x for _, x in c)) // 2,
        )
        for _, _, c in others
    ]
    for i, (y1, x1) in enumerate(centers):
        for y2, x2 in centers[i + 1 :]:
            steps = max(abs(y2 - y1), abs(x2 - x1))
            if steps:
                for step in range(steps + 1):
                    y = y1 + round((y2 - y1) * step / steps)
                    x = x1 + round((x2 - x1) * step / steps)
                    out[y][x] = line_color
    return out
