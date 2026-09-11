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

    cores, boxes = {}, {}
    for color in colors - {bg}:
        parts = components(color)
        if not parts:
            return a
        core = max(parts, key=len)
        ys, xs = zip(*core)
        top, bottom, left, right = min(ys), max(ys), min(xs), max(xs)
        if len(core) != (bottom - top + 1) * (right - left + 1):
            return a
        cores[color], boxes[color] = set(core), (top, bottom, left, right)

    out = [[bg] * w for _ in range(h)]
    for color, core in cores.items():
        for y, x in core:
            out[y][x] = color
        top, bottom, left, right = boxes[color]
        for y in range(h):
            for x in range(w):
                if a[y][x] != color or (y, x) in core:
                    continue
                rd = top - y if y < top else y - bottom if y > bottom else 0
                cd = left - x if x < left else x - right if x > right else 0
                if rd >= cd and rd:
                    ty, tx = (top - 1 if y < top else bottom + 1), min(max(x, left), right)
                elif cd:
                    ty, tx = min(max(y, top), bottom), (left - 1 if x < left else right + 1)
                else:
                    continue
                if 0 <= ty < h and 0 <= tx < w:
                    out[ty][tx] = color
    return out
