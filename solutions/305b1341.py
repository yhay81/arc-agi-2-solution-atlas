def solve(grid):
    if not grid or not grid[0] or grid[0][0] == 0:
        return [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    key_cells = {(0, 0)}
    pending = [(0, 0)]
    while pending:
        row, col = pending.pop()
        for drow, dcol in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_row, next_col = (row + drow, col + dcol)
            if (
                0 <= next_row < height
                and 0 <= next_col < width
                and grid[next_row][next_col] != 0
                and ((next_row, next_col) not in key_cells)
            ):
                key_cells.add((next_row, next_col))
                pending.append((next_row, next_col))
    key_top = min((row for row, _ in key_cells))
    key_bottom = max((row for row, _ in key_cells))
    key_left = min((col for _, col in key_cells))
    key_right = max((col for _, col in key_cells))
    key = [row[key_left : key_right + 1] for row in grid[key_top : key_bottom + 1]]
    if any(value == 0 for row in key for value in row) or len(key[0]) != 2:
        return [row[:] for row in grid]
    mapping = {row[0]: row[1] for row in key}
    source = [row[:] for row in grid]
    for row, col in key_cells:
        source[row][col] = 0
    objects = []
    for foreground, background in mapping.items():
        points = [(r, c) for r in range(height) for c in range(width) if source[r][c] == foreground]
        if not len(points):
            continue
        top, left = min(row for row, _ in points), min(col for _, col in points)
        bottom, right = max(row for row, _ in points), max(col for _, col in points)
        if any((row - top) % 2 for row, _ in points) or any((col - left) % 2 for _, col in points):
            return [row[:] for row in grid]
        objects.append((top, left, foreground, background, points))
    if not objects:
        return [row[:] for row in grid]
    output = [[0] * width for _ in range(height)]
    for top, left, foreground, background, points in sorted(objects):
        bottom, right = max(row for row, _ in points), max(col for _, col in points)
        target_top, target_left = (top - 1, left - 1)
        target_bottom, target_right = (int(bottom) + 1, int(right) + 1)
        if target_top < 0 or target_left < 0 or target_bottom >= height or (target_right >= width):
            return [row[:] for row in grid]
        for r in range(target_top, target_bottom + 1):
            for c in range(target_left, target_right + 1):
                output[r][c] = background
        for row, col in points:
            output[row][col] = foreground
    return output
