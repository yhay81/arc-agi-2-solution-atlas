def solve(grid):
    height, width = len(grid), len(grid[0])
    glyph = {(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 7}
    dots = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 2]
    output = [[1] * width for _ in range(height)]
    vertical = horizontal = None
    sides = set()
    for row, col in dots:
        if row in (0, height - 1):
            vertical = col
            sides.add("top" if row == 0 else "bottom")
            ys = [r for r, c in glyph if c == col]
            stop = max(ys) if row == 0 else min(ys)
            for r in range(min(row, stop), max(row, stop) + 1):
                output[r][col] = 2
        elif col in (0, width - 1):
            horizontal = row
            sides.add("left" if col == 0 else "right")
            xs = [c for r, c in glyph if r == row]
            stop = max(xs) if col == 0 else min(xs)
            for c in range(min(col, stop), max(col, stop) + 1):
                output[row][c] = 2
    for vert in ("top", "bottom"):
        for horiz in ("left", "right"):
            if vert not in sides and horiz not in sides:
                continue
            points = [
                (r, c)
                for r, c in glyph
                if (horizontal is None or (r < horizontal if vert == "top" else r > horizontal))
                and (vertical is None or (c < vertical if horiz == "left" else c > vertical))
            ]
            if not points:
                continue
            top, bottom = min(r for r, _ in points), max(r for r, _ in points)
            left, right = min(c for _, c in points), max(c for _, c in points)
            row_shift = -top if vert == "top" else height - 1 - bottom
            col_shift = -left if horiz == "left" else width - 1 - right
            for r, c in points:
                output[r + row_shift][c + col_shift] = 7
    for r, c in glyph:
        if (vertical is not None and c == vertical) or (horizontal is not None and r == horizontal):
            output[r][c] = 7
    return output
