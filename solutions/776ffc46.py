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

    refs = []
    for frame in colors - {bg}:
        for comp in components(frame):
            if len(comp) < 8:
                continue
            ys, xs = zip(*comp)
            top, bottom, left, right = min(ys), max(ys), min(xs), max(xs)
            perimeter = {(top, x) for x in range(left, right + 1)} | {
                (bottom, x) for x in range(left, right + 1)
            }
            perimeter |= {(y, left) for y in range(top, bottom + 1)} | {
                (y, right) for y in range(top, bottom + 1)
            }
            if bottom - top < 2 or right - left < 2 or set(comp) != perimeter:
                continue
            interior = [(y, x) for y in range(top + 1, bottom) for x in range(left + 1, right)]
            for color in colors - {bg, frame}:
                cells = [(y, x) for y, x in interior if a[y][x] == color]
                if cells:
                    my, mx = min(y for y, _ in cells), min(x for _, x in cells)
                    sig = tuple(sorted((y - my, x - mx) for y, x in cells))
                    refs.append((sig, color, set(comp)))
    if not refs:
        return a
    out = [row[:] for row in a]
    for color in colors - {bg}:
        for comp in components(color):
            cells = set(comp)
            if any(cells & frame for _, _, frame in refs):
                continue
            my, mx = min(y for y, _ in comp), min(x for _, x in comp)
            sig = tuple(sorted((y - my, x - mx) for y, x in comp))
            for ref_sig, target, _ in refs:
                if sig == ref_sig and color != target:
                    for y, x in comp:
                        out[y][x] = target
                    break
    return out
