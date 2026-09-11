def solve(grid):
    h, w = len(grid), len(grid[0])
    positions = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    if len(positions) < 8:
        return [row[:] for row in grid]
    top, left = min(r for r, _ in positions), min(c for _, c in positions)
    bottom, right = max(r for r, _ in positions), max(c for _, c in positions)
    if bottom - top < 3 or right - left < 3:
        return [row[:] for row in grid]
    if not (
        all(grid[top][c] == 5 for c in range(left, right + 1))
        and all(grid[bottom][c] == 5 for c in range(left, right + 1))
        and all(grid[r][left] == 5 for r in range(top, bottom + 1))
        and all(grid[r][right] == 5 for r in range(top, bottom + 1))
    ):
        return [row[:] for row in grid]
    outside = [
        ((r, c), grid[r][c])
        for r in range(h)
        for c in range(w)
        if grid[r][c] != 0 and not (top <= r <= bottom and left <= c <= right) and grid[r][c] != 5
    ]
    colors = []
    for _, color in outside:
        if color not in colors:
            colors.append(color)
    if len(colors) != 2:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    marker_a = outside[0]
    marker_b = next(item for item in outside[1:] if item[1] != marker_a[1])
    (row_a, col_a), color_a = marker_a
    (row_b, col_b), color_b = marker_b
    row_mid = (top + bottom) / 2
    col_mid = (left + right) / 2
    if abs(row_a - row_b) <= abs(col_a - col_b):
        left_color, right_color = (color_a, color_b) if col_a < col_b else (color_b, color_a)
        if (row_a + row_b) / 2 > bottom:
            left_color, right_color = (right_color, left_color)
        for row in range(top + 1, bottom):
            for col in range(left + 1, right):
                output[row][col] = left_color if (row < row_mid) == (col < col_mid) else right_color
    else:
        top_color, bottom_color = (color_a, color_b) if row_a < row_b else (color_b, color_a)
        right_side = (col_a + col_b) / 2 > col_mid
        for row in range(top + 1, bottom):
            for col in range(left + 1, right):
                same_half = (row < row_mid) == (col < col_mid)
                if right_side:
                    output[row][col] = bottom_color if same_half else top_color
                else:
                    output[row][col] = top_color if same_half else bottom_color
    return output
