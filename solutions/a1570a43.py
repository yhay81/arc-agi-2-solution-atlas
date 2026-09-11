def solve(grid):
    height, width = len(grid), len(grid[0])
    values = sorted({value for row in grid for value in row})
    counts = {value: sum(row.count(value) for row in grid) for value in values}
    background = max(values, key=lambda value: counts[value])
    output = [row[:] for row in grid]
    for marker in values:
        if marker == background:
            continue
        markers = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == marker]
        if len(markers) != 4:
            continue
        top, bottom = min(r for r, _ in markers), max(r for r, _ in markers)
        left, right = min(c for _, c in markers), max(c for _, c in markers)
        if set(markers) != {(top, left), (top, right), (bottom, left), (bottom, right)}:
            continue
        inner_height, inner_width = bottom - top - 1, right - left - 1
        if inner_height <= 0 or inner_width <= 0:
            continue
        for color in values:
            if color in (background, marker):
                continue
            cells = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == color]
            if not cells:
                continue
            shape_top, shape_bottom = min(r for r, _ in cells), max(r for r, _ in cells)
            shape_left, shape_right = min(c for _, c in cells), max(c for _, c in cells)
            shape_height, shape_width = shape_bottom - shape_top + 1, shape_right - shape_left + 1
            if shape_height > inner_height or shape_width > inner_width:
                continue
            for r, c in cells:
                output[r][c] = background
            row_shift = top + 1 + (inner_height - shape_height) // 2 - shape_top
            col_shift = left + 1 + (inner_width - shape_width) // 2 - shape_left
            for r, c in cells:
                output[r + row_shift][c + col_shift] = color
    return output
