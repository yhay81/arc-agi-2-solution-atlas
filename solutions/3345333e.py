def solve(grid):
    height, width = len(grid), len(grid[0])
    colors = {value for row in grid for value in row if value}
    if len(colors) != 2:
        return [row[:] for row in grid]
    boxes = []
    for color in colors:
        cells = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == color]
        top, bottom = min(r for r, _ in cells), max(r for r, _ in cells)
        left, right = min(c for _, c in cells), max(c for _, c in cells)
        if len(cells) >= 4 and len(cells) == (bottom - top + 1) * (right - left + 1):
            boxes.append(color)
    if len(boxes) != 1:
        return [row[:] for row in grid]
    occluder = boxes[0]
    pattern = next(color for color in colors if color != occluder)
    cells = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == pattern]
    candidates = []
    for axis in range(2 * width - 1):
        paired = hidden = 0
        for row, col in cells:
            mirror = axis - col
            if not 0 <= mirror < width or grid[row][mirror] not in (pattern, occluder):
                break
            paired += grid[row][mirror] == pattern
            hidden += grid[row][mirror] == occluder
        else:
            if hidden:
                candidates.append((paired, axis))
    if not candidates:
        return [row[:] for row in grid]
    score = max(pair for pair, _ in candidates)
    axes = [axis for pair, axis in candidates if pair == score]
    if len(axes) != 1:
        return [row[:] for row in grid]
    output = [[0 if value == occluder else value for value in row] for row in grid]
    for row, col in cells:
        output[row][axes[0] - col] = pattern
    return output
