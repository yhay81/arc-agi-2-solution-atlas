def solve(grid):
    a = [list(map(int, row)) for row in grid]
    h, w = len(a), len(a[0]) if a else 0
    if not h or not w:
        return a
    colors = {v for row in a for v in row}
    bg = max(colors, key=lambda c: sum(v == c for row in a for v in row))

    seen, parts = set(), []
    for r in range(h):
        for c in range(w):
            if a[r][c] == bg or (r, c) in seen:
                continue
            stack, comp = [(r, c)], []
            seen.add((r, c))
            while stack:
                y, x = stack.pop()
                comp.append((y, x))
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        ny, nx = y + dy, x + dx
                        if (
                            (dy or dx)
                            and 0 <= ny < h
                            and 0 <= nx < w
                            and a[ny][nx] != bg
                            and (ny, nx) not in seen
                        ):
                            seen.add((ny, nx))
                            stack.append((ny, nx))
            parts.append(comp)
    hubs = [p for p in parts if len({a[y][x] for y, x in p}) == 4]
    if len(hubs) != 1:
        return a
    hub = hubs[0]
    ys, xs = zip(*hub)
    top, bottom, left, right = min(ys), max(ys), min(xs), max(xs)
    out = [[bg] * w for _ in range(h)]
    for y, x in hub:
        out[y][x] = a[y][x]
    sides = [
        [p for p in hub if p[0] == top],
        [p for p in hub if p[0] == bottom],
        [p for p in hub if p[1] == left],
        [p for p in hub if p[1] == right],
    ]
    if any(len(side) != 2 for side in sides):
        return a
    for side, contact in enumerate(sides):
        color = a[contact[0][0]][contact[0][1]]
        for part in parts:
            if any(a[y][x] != color for y, x in part):
                continue
            for turns in range(4):
                q = part[:]
                for _ in range(turns):
                    q = [(x, -y) for y, x in q]
                min_y, min_x = min(y for y, _ in q), min(x for _, x in q)
                q = [(y - min_y, x - min_x) for y, x in q]
                hh, ww = max(y for y, _ in q) + 1, max(x for _, x in q) + 1
                if side < 2:
                    edge = [x for y, x in q if y == (hh - 1 if side == 0 else 0)]
                    if len(edge) != 2 or sorted(edge) != [ww // 2 - 1, ww // 2] or ww % 2:
                        continue
                    off_y = top - hh if side == 0 else bottom + 1
                    off_x = min(x for _, x in contact) - min(edge)
                else:
                    edge = [y for y, x in q if x == (ww - 1 if side == 2 else 0)]
                    if len(edge) != 2 or sorted(edge) != [hh // 2 - 1, hh // 2] or hh % 2:
                        continue
                    off_y = min(y for y, _ in contact) - min(edge)
                    off_x = left - ww if side == 2 else right + 1
                shifted = [(y + off_y, x + off_x) for y, x in q]
                if all(0 <= y < h and 0 <= x < w for y, x in shifted):
                    for y, x in shifted:
                        out[y][x] = color
                    break
    return out
