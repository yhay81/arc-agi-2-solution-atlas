def solve(grid):
    height, width = len(grid), len(grid[0])
    for frame in {value for row in grid for value in row if value}:
        cells = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == frame}
        top, bottom = min(r for r, _ in cells), max(r for r, _ in cells)
        left, right = min(c for _, c in cells), max(c for _, c in cells)
        perimeter = {(top, c) for c in range(left, right + 1)} | {
            (bottom, c) for c in range(left, right + 1)
        }
        perimeter |= {(r, left) for r in range(top, bottom + 1)} | {
            (r, right) for r in range(top, bottom + 1)
        }
        if bottom - top < 2 or right - left < 2 or cells != perimeter:
            continue
        glyph = [
            (r, c, grid[r][c])
            for r in range(height)
            for c in range(width)
            if grid[r][c] not in (0, frame)
        ]
        if not glyph:
            continue
        glyph_top, glyph_bottom = min(r for r, _, _ in glyph), max(r for r, _, _ in glyph)
        glyph_left, glyph_right = min(c for _, c, _ in glyph), max(c for _, c, _ in glyph)
        source = [
            [
                grid[r][c] if grid[r][c] not in (0, frame) else 0
                for c in range(glyph_left, glyph_right + 1)
            ]
            for r in range(glyph_top, glyph_bottom + 1)
        ]
        inner_height, inner_width = bottom - top - 1, right - left - 1
        if inner_height % len(source) or inner_width % len(source[0]):
            continue
        row_scale, col_scale = inner_height // len(source), inner_width // len(source[0])
        scaled = [
            [source[r // row_scale][c // col_scale] for c in range(inner_width)]
            for r in range(inner_height)
        ]
        output = [row[left : right + 1] for row in grid[top : bottom + 1]]
        for row, values in enumerate(scaled, 1):
            output[row][1:-1] = values
        return output
    return [row[:] for row in grid]
