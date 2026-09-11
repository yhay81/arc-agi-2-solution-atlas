def solve(grid):
    a = [list(map(int, row)) for row in grid]
    h, w = len(a), len(a[0]) if a else 0
    if not h or not w:
        return a
    colors = {v for row in a for v in row}
    bg = max(colors, key=lambda c: sum(v == c for row in a for v in row))
    seen, glyphs, bars = set(), [], []
    for r in range(h):
        for c in range(w):
            if a[r][c] == bg or (r, c) in seen:
                continue
            stack, cells = [(r, c)], []
            seen.add((r, c))
            while stack:
                y, x = stack.pop()
                cells.append((y, x))
                for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                    if 0 <= ny < h and 0 <= nx < w and a[ny][nx] != bg and (ny, nx) not in seen:
                        seen.add((ny, nx))
                        stack.append((ny, nx))
            ys, xs = zip(*cells)
            top, left, bottom, right = min(ys), min(xs), max(ys), max(xs)
            rel = {(y - top, x - left) for y, x in cells}
            glyph_shape = (
                {(0, x) for x in range(1, 4)}
                | {(1, x) for x in range(5)}
                | {(2, x) for x in range(1, 4)}
            )
            if len(cells) == 11 and (bottom - top, right - left) == (2, 4) and rel == glyph_shape:
                glyphs.append((top, left, a[top][left], cells))
            elif len(cells) == 5 and top == bottom and right - left == 4:
                bars.append((top, left, a[top][left], cells))
    if not glyphs or not bars:
        return a

    def column_for(left):
        center = left + 2
        inside = [gleft for _, gleft, _, _ in glyphs if gleft <= center <= gleft + 4]
        return (
            inside[0] if inside else min({g[1] for g in glyphs}, key=lambda x: abs(x + 2 - center))
        )

    bar_columns = [(color, column_for(left)) for _, left, color, _ in bars]
    out = [row[:] for row in a]
    for _, _, _, cells in bars:
        for y, x in cells:
            out[y][x] = bg
    repaint = {column for color, column in bar_columns if color == 2}
    extend = {column for color, column in bar_columns if color == 3}
    count = sum(gleft in repaint for _, gleft, _, _ in glyphs)
    for top, left, _, cells in glyphs:
        if left in repaint:
            for y, x in cells:
                out[y][x] = 5
    for left in extend:
        sources = [g for g in glyphs if g[1] == left]
        if not sources:
            continue
        top, source_left, _, cells = min(sources, key=lambda g: g[0])
        for i in range(1, count + 1):
            copy_top = top - 4 * i
            for y, x in cells:
                ty, tx = copy_top + y - top, source_left + x - source_left
                if 0 <= ty < h and 0 <= tx < w:
                    out[ty][tx] = a[y][x]
    return out
