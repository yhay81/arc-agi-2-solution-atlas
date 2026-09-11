def solve(grid):
    a = [list(map(int, row)) for row in grid]
    h, w = len(a), len(a[0]) if a else 0
    if not h or not w:
        return a
    seen, glyphs, singles = set(), [], []
    for r in range(h):
        for c in range(w):
            if a[r][c] == 0 or (r, c) in seen:
                continue
            stack, comp = [(r, c)], []
            seen.add((r, c))
            while stack:
                y, x = stack.pop()
                comp.append((y, x))
                for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                    if 0 <= ny < h and 0 <= nx < w and a[ny][nx] != 0 and (ny, nx) not in seen:
                        seen.add((ny, nx))
                        stack.append((ny, nx))
            if len(comp) == 1:
                y, x = comp[0]
                singles.append((y, x, a[y][x]))
                continue
            vals = {a[y][x] for y, x in comp}
            unique = [v for v in vals if sum(a[y][x] == v for y, x in comp) == 1]
            if len(vals) != 2 or len(unique) != 1:
                continue
            key = unique[0]
            ky, kx = next((y, x) for y, x in comp if a[y][x] == key)
            glyphs.append((key, ky, kx, [(y, x, a[y][x]) for y, x in comp if a[y][x] != key]))
    if not glyphs:
        return a
    out = [row[:] for row in a]
    for key, ky, kx, body in glyphs:
        anchors = [(y, x) for y, x, color in singles if color == key and (y, x) != (ky, kx)]
        for ay, ax in anchors:
            for y, x, color in body:
                dy, dx = y - ky, x - kx
                if key == 2:
                    dx = -dx
                ty, tx = ay + dy, ax + dx
                if 0 <= ty < h and 0 <= tx < w:
                    out[ty][tx] = color
    if len(glyphs) == 1:
        key, ky, kx, _ = glyphs[0]
        anchors = [(y, x) for y, x, color in singles if color == key and (y, x) != (ky, kx)]
        for y, x, color in singles:
            if color == key:
                continue
            dy, dx = y - ky, x - kx
            if key == 2:
                dx = -dx
            for ay, ax in anchors:
                ty, tx = ay + dy, ax + dx
                if 0 <= ty < h and 0 <= tx < w:
                    out[ty][tx] = color
    return out
