def solve(grid):
    h, w = len(grid), len(grid[0])
    frame_color = -1
    fill_color = -1
    marker_color = 8
    markers = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == marker_color]
    if len(markers) != 1:
        return [row[:] for row in grid]
    positions = [(r, c) for r in range(h) for c in range(w) if grid[r][c] not in (0, marker_color)]
    if not len(positions):
        return [row[:] for row in grid]
    top, left = min(r for r, _ in positions), min(c for _, c in positions)
    bottom, right = max(r for r, _ in positions), max(c for _, c in positions)
    if bottom - top < 2 or right - left < 2:
        return [row[:] for row in grid]
    if frame_color < 0 or fill_color < 0:
        border_values = {
            grid[row][col]
            for row in range(top, bottom + 1)
            for col in range(left, right + 1)
            if row in (top, bottom) or col in (left, right)
        }
        interior_values = {
            grid[row][col] for row in range(top + 1, bottom) for col in range(left + 1, right)
        }
        if len(border_values) != 1 or len(interior_values) != 1:
            return [row[:] for row in grid]
        frame_color = next(iter(border_values))
        fill_color = next(iter(interior_values))
    for row in range(top, bottom + 1):
        for col in range(left, right + 1):
            perimeter = row in (top, bottom) or col in (left, right)
            expected = int(frame_color) if perimeter else int(fill_color)
            if grid[row][col] != expected:
                return [row[:] for row in grid]
    if any(grid[row][col] == 0 for row in range(top, bottom + 1) for col in range(left, right + 1)):
        return [row[:] for row in grid]
    marker_row, marker_col = markers[0]
    new_top, new_left, new_bottom, new_right = (top, left, bottom, right)
    if top <= marker_row <= bottom and marker_col > right:
        new_right = marker_col
    elif top <= marker_row <= bottom and marker_col < left:
        new_left = marker_col
    elif left <= marker_col <= right and marker_row > bottom:
        new_bottom = marker_row
    elif left <= marker_col <= right and marker_row < top:
        new_top = marker_row
    else:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for row in range(new_top, new_bottom + 1):
        for col in range(new_left, new_right + 1):
            output[row][col] = (
                frame_color
                if row in (new_top, new_bottom) or col in (new_left, new_right)
                else fill_color
            )
    return output
