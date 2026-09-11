def solve(grid):
    a = [list(map(int, row)) for row in grid]
    h, w = len(a), len(a[0]) if a else 0
    if not h or not w:
        return a
    values = {v for row in a for v in row}
    counts = {v: sum(x == v for row in a for x in row) for v in values}
    bg = max(values, key=lambda v: counts[v])
    frames = []
    for color in values - {bg}:
        pos = [(r, c) for r in range(h) for c in range(w) if a[r][c] == color]
        top, left = min(r for r, _ in pos), min(c for _, c in pos)
        bottom, right = max(r for r, _ in pos), max(c for _, c in pos)
        perimeter = {(top, c) for c in range(left, right + 1, 2)} | {
            (bottom, c) for c in range(left, right + 1, 2)
        }
        perimeter |= {(r, left) for r in range(top, bottom + 1, 2)} | {
            (r, right) for r in range(top, bottom + 1, 2)
        }
        if (
            bottom > top
            and right > left
            and (bottom - top) % 2 == 0
            and (right - left) % 2 == 0
            and len(perimeter) >= 8
            and set(pos) == perimeter
        ):
            frames.append((color, top, bottom, left, right))
    if len(frames) != 1:
        return a
    frame, top, bottom, left, right = frames[0]
    nonframe = [(counts[v], v) for v in values if v not in (bg, frame)]
    if not nonframe:
        return a
    lattice = max(nonframe)[1]
    payload = [v for _, v in nonframe if v != lattice]
    if not payload:
        return a
    glyphs = []
    for color in payload:
        pos = [
            (r, c)
            for r in range(h)
            for c in range(w)
            if a[r][c] == color and not (top <= r <= bottom and left <= c <= right)
        ]
        if not pos:
            return a
        gt, gl = min(r for r, _ in pos), min(c for _, c in pos)
        gb, gr = max(r for r, _ in pos), max(c for _, c in pos)
        glyphs.append((gt, gl, gb - gt + 1, gr - gl + 1, color))
    ih, iw = bottom - top - 1, right - left - 1
    heights, widths = {g[2] for g in glyphs}, {g[3] for g in glyphs}
    horizontal = len(heights) == 1 and sum(g[3] for g in glyphs) + len(glyphs) - 1 <= iw
    vertical = len(widths) == 1 and sum(g[2] for g in glyphs) + len(glyphs) - 1 <= ih
    if horizontal == vertical:
        return a
    glyphs.sort(key=lambda g: (g[1], g[0]) if horizontal else (g[0], g[1]))
    out = [row[:] for row in a]
    for color in payload:
        for r in range(h):
            for c in range(w):
                if out[r][c] == color:
                    out[r][c] = bg
    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            out[r][c] = bg
    for c in range(left, right + 1):
        out[top][c] = out[bottom][c] = frame
    for r in range(top, bottom + 1):
        out[r][left] = out[r][right] = frame
    if horizontal:
        total = sum(g[3] for g in glyphs) + len(glyphs) - 1
        row, col = top + 1 + (ih - next(iter(heights))) // 2, left + 1 + (iw - total) // 2
        for _, _, gh, gw, color in glyphs:
            for r in range(row, row + gh):
                for c in range(col, col + gw):
                    out[r][c] = color
            col += gw + 1
    else:
        total = sum(g[2] for g in glyphs) + len(glyphs) - 1
        row, col = top + 1 + (ih - total) // 2, left + 1 + (iw - next(iter(widths))) // 2
        for _, _, gh, gw, color in glyphs:
            for r in range(row, row + gh):
                for c in range(col, col + gw):
                    out[r][c] = color
            row += gh + 1
    return out
