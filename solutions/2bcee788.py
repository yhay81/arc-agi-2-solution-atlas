def solve(grid):
    h, w = len(grid), len(grid[0])
    marker_color = 2
    background_color = 3
    colors = {value for row in grid for value in row if value != 0}
    shape_colors = colors - {marker_color}
    marker_positions = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == marker_color]
    if len(shape_colors) != 1 or not len(marker_positions):
        return [row[:] for row in grid]
    shape_color = next(iter(shape_colors))
    shape_positions = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == shape_color]
    if not len(shape_positions):
        return [row[:] for row in grid]
    top, left = min(r for r, _ in shape_positions), min(c for _, c in shape_positions)
    bottom, right = max(r for r, _ in shape_positions), max(c for _, c in shape_positions)
    marker_set = set(marker_positions)
    orientations = []
    edge_top = {(top, col) for col in range(w) if grid[top][col] == shape_color}
    edge_bottom = {(bottom, col) for col in range(w) if grid[bottom][col] == shape_color}
    edge_left = {(row, left) for row in range(h) if grid[row][left] == shape_color}
    edge_right = {(row, right) for row in range(h) if grid[row][right] == shape_color}
    if top > 0:
        orientations.append(("top", {(top - 1, col) for _, col in edge_top}, top - 1))
    if bottom + 1 < h:
        orientations.append(("bottom", {(bottom + 1, col) for _, col in edge_bottom}, bottom + 1))
    if left > 0:
        orientations.append(("left", {(row, left - 1) for row, _ in edge_left}, left - 1))
    if right + 1 < w:
        orientations.append(("right", {(row, right + 1) for row, _ in edge_right}, right + 1))
    matching = [
        (side, expected, hinge) for side, expected, hinge in orientations if marker_set == expected
    ]
    if len(matching) != 1:
        return [row[:] for row in grid]
    side, _, hinge = matching[0]
    output = [[background_color] * w for _ in range(h)]
    for row, col in shape_positions:
        output[row][col] = shape_color
    for row, col in shape_positions:
        if side in ("top", "bottom"):
            reflected_row = 2 * hinge + 1 - row if side == "top" else 2 * hinge - 1 - row
            reflected_col = col
        else:
            reflected_row = row
            reflected_col = 2 * hinge + 1 - col if side == "left" else 2 * hinge - 1 - col
        if 0 <= reflected_row < h and 0 <= reflected_col < w:
            output[reflected_row][reflected_col] = shape_color
    return output
