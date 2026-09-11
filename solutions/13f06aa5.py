def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = {color: sum(row.count(color) for row in grid) for color in range(10)}
    background = max(counts, key=lambda color: (counts[color], -color))
    markers = []
    for color in range(1, 10):
        if counts[color] != 1:
            continue
        row, col = next((r, c) for r in range(height) for c in range(width) if grid[r][c] == color)
        neighbours = (
            (row - 1, col, "up"),
            (row + 1, col, "down"),
            (row, col - 1, "left"),
            (row, col + 1, "right"),
        )
        present = {
            direction
            for r, c, direction in neighbours
            if 0 <= r < height and 0 <= c < width and grid[r][c] not in (background, color)
        }
        orientation = None
        if {"left", "right", "down"} <= present and "up" not in present:
            orientation = "top"
        elif {"left", "right", "up"} <= present and "down" not in present:
            orientation = "bottom"
        elif {"up", "down", "right"} <= present and "left" not in present:
            orientation = "left"
        elif {"up", "down", "left"} <= present and "right" not in present:
            orientation = "right"
        if orientation:
            markers.append((row, col, color, orientation))
    if not markers:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    has_left = any(orientation == "left" for *_, orientation in markers)
    has_right = any(orientation == "right" for *_, orientation in markers)
    left_edge, right_edge = (1 if has_left else 0), (width - 2 if has_right else width - 1)
    for row, col, color, orientation in markers:
        if orientation in ("top", "bottom"):
            edge_row = 0 if orientation == "top" else height - 1
            for c in range(left_edge, right_edge + 1):
                output[edge_row][c] = color
            step = -2 if orientation == "top" else 2
            ray_row = row + step
            while 0 <= ray_row < height:
                output[ray_row][col] = color
                ray_row += step
            if has_left:
                output[edge_row][0] = 0
            if has_right:
                output[edge_row][width - 1] = 0
        elif orientation == "left":
            for r in range(1, height):
                output[r][0] = color
            ray_col = col - 2
            while ray_col >= 0:
                output[row][ray_col] = color
                ray_col -= 2
        else:
            for r in range(1, height):
                output[r][width - 1] = color
            ray_col = col + 2
            while ray_col < width:
                output[row][ray_col] = color
                ray_col += 2
    return output
