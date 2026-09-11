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

    moves, seen_markers = [], set()
    for r in range(h):
        for c in range(w):
            if a[r][c] != 8 or (r, c) in seen_markers:
                continue
            neighbors = [
                (y, x)
                for y, x in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
                if 0 <= y < h and 0 <= x < w and a[y][x] not in (bg, 8)
            ]
            if not neighbors:
                continue
            body_color = max(
                {a[y][x] for y, x in neighbors},
                key=lambda color: sum(a[y][x] == color for y, x in neighbors),
            )
            body = next(
                (part for part in components(body_color) if set(part) & set(neighbors)), None
            )
            if body is None:
                continue
            cells = set(body) | {(r, c)}
            ys, xs = zip(*cells)
            cr, cc = (min(ys) + max(ys)) / 2, (min(xs) + max(xs)) / 2
            dr = 1 if r > cr else -1 if r < cr else 0
            dc = 1 if c > cc else -1 if c < cc else 0
            moves.append((cells, body_color, dr, dc))
            seen_markers.add((r, c))
    if not moves:
        return a
    out = [row[:] for row in a]
    for cells, _, _, _ in moves:
        for y, x in cells:
            out[y][x] = bg
    for cells, color, dr, dc in moves:
        for y, x in cells:
            ty, tx = y + dr, x + dc
            if 0 <= ty < h and 0 <= tx < w:
                out[ty][tx] = color
    return out
