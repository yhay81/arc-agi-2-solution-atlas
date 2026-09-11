def solve(grid):
    h, w = len(grid), len(grid[0]) if grid else 0
    colors = sorted({v for row in grid for v in row if v})
    if len(colors) != 2:
        return [r[:] for r in grid]
    bounds = {}
    for color in colors:
        cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == color]
        bounds[color] = (
            min(r for r, c in cells),
            min(c for r, c in cells),
            max(r for r, c in cells),
            max(c for r, c in cells),
        )
    guide_color = max(colors, key=lambda c: bounds[c][0])
    target = next(c for c in colors if c != guide_color)
    gt, gl, gb, gr = bounds[guide_color]
    guide = [[grid[r][c] == guide_color for c in range(gl, gr + 1)] for r in range(gt, gb + 1)]
    full = [r for r, row in enumerate(guide) if all(row)]
    if not full or full[0] == 0:
        return [r[:] for r in grid]
    upper = [(r, c) for r in range(full[0]) for c, v in enumerate(guide[r]) if v]
    if not upper:
        return [r[:] for r in grid]
    center = (len(guide[0]) - 1) / 2
    mean = sum(c for _, c in upper) / len(upper)
    if mean == center:
        return [r[:] for r in grid]
    direction = -1 if mean < center else 1
    top, left, bottom, right = bounds[target]
    glyph = [row[left : right + 1] for row in grid[top : bottom + 1]]
    mirrored = [row[::-1] for row in glyph]
    width = len(glyph[0])
    start = left - width if direction < 0 else right + 1
    if start < 0 or start + width > w:
        return [r[:] for r in grid]
    out = [r[:] for r in grid]
    for r, row in enumerate(mirrored):
        for c, v in enumerate(row):
            if v:
                out[top + r][start + c] = v
    return out
