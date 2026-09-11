def solve(grid):
    height, width = len(grid), len(grid[0])
    lines = []
    for row in range(height):
        color = grid[row][0]
        if (
            color
            and all(value == color for value in grid[row])
            and sum(value == color for line in grid for value in line) == width
        ):
            lines.append(("horizontal", row, color))
    for col in range(width):
        color = grid[0][col]
        if (
            color
            and all(grid[r][col] == color for r in range(height))
            and sum(value == color for line in grid for value in line) == height
        ):
            lines.append(("vertical", col, color))
    if len(lines) != 1:
        return [row[:] for row in grid]
    axis, line_position, line_color = lines[0]
    object_colors = {value for row in grid for value in row if value not in (0, line_color)}
    if len(object_colors) != 1:
        return [row[:] for row in grid]
    object_cells = [
        (r, c) for r in range(height) for c in range(width) if grid[r][c] not in (0, line_color)
    ]
    if not object_cells:
        return [row[:] for row in grid]
    output = [[0] * width for _ in range(height)]
    if axis == "horizontal":
        output[line_position] = [line_color] * width
        top, bottom = min(r for r, _ in object_cells), max(r for r, _ in object_cells)
        object_height = bottom - top + 1
        if bottom < line_position:
            new_top, backstop = (line_position - object_height, line_position - object_height - 1)
        elif top > line_position:
            new_top, backstop = (line_position + 1, line_position + object_height + 1)
        else:
            return [row[:] for row in grid]
        if not 0 <= backstop < height:
            return [row[:] for row in grid]
        for row, col in object_cells:
            output[new_top + row - top][col] = grid[row][col]
        output[backstop] = [8] * width
    else:
        for row in range(height):
            output[row][line_position] = line_color
        left, right = min(c for _, c in object_cells), max(c for _, c in object_cells)
        object_width = right - left + 1
        if right < line_position:
            new_left, backstop = (line_position - object_width, line_position - object_width - 1)
        elif left > line_position:
            new_left, backstop = (line_position + 1, line_position + object_width + 1)
        else:
            return [row[:] for row in grid]
        if not 0 <= backstop < width:
            return [row[:] for row in grid]
        for row, col in object_cells:
            output[row][new_left + col - left] = grid[row][col]
        for row in range(height):
            output[row][backstop] = 8
    return output
