def solve(grid):
    a = [list(map(int, row)) for row in grid]
    h, w = len(a), len(a[0]) if a else 0
    if not h or not w:
        return a
    colors = {v for row in a for v in row}
    bg = max(colors, key=lambda c: sum(v == c for row in a for v in row))
    out = [row[:] for row in a]

    def components(color):
        seen, found = set(), []
        for r in range(h):
            for c in range(w):
                if out[r][c] != color or (r, c) in seen:
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
                                and out[ny][nx] == color
                                and (ny, nx) not in seen
                            ):
                                seen.add((ny, nx))
                                stack.append((ny, nx))
                found.append(part)
        return found

    for edge, direction in ((0, -1), (w - 1, 1)):
        edge_colors = {out[r][edge] for r in range(h) if out[r][edge] != bg}
        if len(edge_colors) != 1:
            continue
        color = next(iter(edge_colors))
        while True:
            parts = components(color)
            if len(parts) <= 1:
                break
            parts.sort(
                key=lambda p: min(x for _, x in p) if direction < 0 else max(x for _, x in p)
            )
            extreme, moving = (parts[0], parts[1]) if direction < 0 else (parts[-1], parts[-2])
            extreme_set = set(extreme)
            shift = None
            for distance in range(1, w + 1):
                shifted = {(y, x + direction * distance) for y, x in moving}
                if any(x < 0 or x >= w for _, x in shifted):
                    break
                if extreme_set & shifted:
                    shift = distance - 1
                    break
            if not shift or shift <= 0:
                break
            for y, x in moving:
                out[y][x] = bg
            for y, x in moving:
                out[y][x + direction * shift] = color
    return out
