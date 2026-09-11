def solve(grid):
    a = [list(map(int, row)) for row in grid]
    h, w = len(a), len(a[0]) if a else 0
    if not h or not w:
        return a
    colors = {v for row in a for v in row}
    bg = max(colors, key=lambda c: sum(v == c for row in a for v in row))
    fg = [c for c in colors if c != bg]
    if len(fg) != 1:
        return a
    color = fg[0]
    seen, out = set(), [row[:] for row in a]
    for r in range(h):
        for c in range(w):
            if a[r][c] != color or (r, c) in seen:
                continue
            stack, comp = [(r, c)], []
            seen.add((r, c))
            while stack:
                y, x = stack.pop()
                comp.append((y, x))
                for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                    if 0 <= ny < h and 0 <= nx < w and a[ny][nx] == color and (ny, nx) not in seen:
                        seen.add((ny, nx))
                        stack.append((ny, nx))
            ys, xs = zip(*comp)
            top, bottom, left, right = min(ys), max(ys), min(xs), max(xs)
            glyph = {(y - top, x - left) for y, x in comp}
            gh, gw = bottom - top + 1, right - left + 1
            vertical = {(y, gw - 1 - x) for y, x in glyph}
            horizontal = {(gh - 1 - y, x) for y, x in glyph}
            if glyph == horizontal and glyph != vertical:
                extra = glyph - vertical
                mid = gw // 2
                left_count = sum(x < mid for _, x in extra)
                right_count = sum(x >= (gw + 1) // 2 for _, x in extra)
                if left_count > right_count:
                    copy_left = left - gw - 1
                elif right_count > left_count:
                    copy_left = right + 2
                else:
                    continue
                for y, x in vertical:
                    ty, tx = top + y, copy_left + x
                    if 0 <= ty < h and 0 <= tx < w and out[ty][tx] == bg:
                        out[ty][tx] = 1
            elif glyph == vertical and glyph != horizontal:
                extra = glyph - horizontal
                mid = gh // 2
                top_count = sum(y < mid for y, _ in extra)
                bottom_count = sum(y >= (gh + 1) // 2 for y, _ in extra)
                if top_count > bottom_count:
                    copy_top = top - gh - 1
                elif bottom_count > top_count:
                    copy_top = bottom + 2
                else:
                    continue
                for y, x in horizontal:
                    ty, tx = copy_top + y, left + x
                    if 0 <= ty < h and 0 <= tx < w and out[ty][tx] == bg:
                        out[ty][tx] = 8
    return out
