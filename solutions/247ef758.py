def solve(grid):
    height, width = len(grid), len(grid[0])
    axis_candidates = [
        col
        for col in range(width)
        if grid[0][col] != 0 and all(grid[row][col] == grid[0][col] for row in range(height))
    ]
    if not axis_candidates:
        return [row[:] for row in grid]
    axis = axis_candidates[0]
    if axis <= 0 or axis >= width - 1:
        return [row[:] for row in grid]
    row_markers: dict[int, list[int]] = {}
    col_markers: dict[int, list[int]] = {}
    for row in range(height):
        color = grid[row][width - 1]
        if color:
            row_markers.setdefault(color, []).append(row)
    for col in range(axis + 1, width):
        color = grid[0][col]
        if color:
            col_markers.setdefault(color, []).append(col)
    output = [row[:] for row in grid]
    glyphs = {}
    for color in sorted({grid[r][c] for r in range(height) for c in range(axis) if grid[r][c]}):
        if color == 0:
            continue
        glyphs[color] = [
            (row, col) for row in range(height) for col in range(axis) if grid[row][col] == color
        ]
    ordered_glyphs = sorted(
        glyphs.items(), key=lambda item: min((row for row, _ in item[1])), reverse=True
    )
    for color, cells in ordered_glyphs:
        if color not in row_markers or color not in col_markers:
            continue
        rows = [row for row, _ in cells]
        cols = [col for _, col in cells]
        center_row = (min(rows) + max(rows)) // 2
        center_col = (min(cols) + max(cols)) // 2
        offsets = [(row - center_row, col - center_col) for row, col in cells]
        for target_row in row_markers[color]:
            for target_col in col_markers[color]:
                for dr, dc in offsets:
                    row, col = (target_row + dr, target_col + dc)
                    if 0 <= row < height and 0 <= col < width:
                        output[row][col] = color
        for row, col in cells:
            output[row][col] = 0
    return output
