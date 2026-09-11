def solve(grid):
    h, w = len(grid), len(grid[0])
    colors = sorted({color for row in grid for color in row if color})
    if len(colors) != 2:
        return [row[:] for row in grid]
    frame_candidates = []
    for color in colors:
        has_square = any(
            all(grid[row + dr][col + dc] == color for dr in (0, 1) for dc in (0, 1))
            for row in range(h - 1)
            for col in range(w - 1)
        )
        has_run = any(
            all(grid[row][col + dc] == color for dc in range(3))
            for row in range(h)
            for col in range(w - 2)
        ) or any(
            all(grid[row + dr][col] == color for dr in range(3))
            for row in range(h - 2)
            for col in range(w)
        )
        if not has_square and has_run:
            frame_candidates.append(color)
    if len(frame_candidates) != 1:
        return [row[:] for row in grid]
    frame_color = frame_candidates[0]
    object_color = next(color for color in colors if color != frame_color)
    positions = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == object_color]
    top, left = min(r for r, _ in positions), min(c for _, c in positions)
    bottom, right = max(r for r, _ in positions), max(c for _, c in positions)
    if len(positions) != (bottom - top + 1) * (right - left + 1):
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for row, col, row_delta, col_delta in (
        (top, left, -1, -1),
        (top, right, -1, 1),
        (bottom, left, 1, -1),
        (bottom, right, 1, 1),
    ):
        row += row_delta
        col += col_delta
        crossed_frame = False
        while 0 <= row < h and 0 <= col < w:
            if grid[row][col] == frame_color:
                crossed_frame = True
            elif crossed_frame and grid[row][col] == 0:
                output[row][col] = object_color
            row += row_delta
            col += col_delta
    return output
