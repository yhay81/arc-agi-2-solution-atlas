def solve(grid):
    height, width = len(grid), len(grid[0])
    candidates = []
    for color in sorted({cell for row in grid for cell in row if cell != 0}):
        components = []
        seen = set()
        for row in range(height):
            for col in range(width):
                if grid[row][col] != color or (row, col) in seen:
                    continue
                stack = [(row, col)]
                seen.add((row, col))
                component = []
                while stack:
                    current_row, current_col = stack.pop()
                    component.append((current_row, current_col))
                    for next_row, next_col in (
                        (current_row - 1, current_col),
                        (current_row + 1, current_col),
                        (current_row, current_col - 1),
                        (current_row, current_col + 1),
                    ):
                        if (
                            0 <= next_row < height
                            and 0 <= next_col < width
                            and grid[next_row][next_col] == color
                            and (next_row, next_col) not in seen
                        ):
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
                components.append(component)
        if len(components) < 2:
            continue
        boxes = []
        shapes = set()
        valid = True
        for component in components:
            top = min(row for row, _ in component)
            bottom = max(row for row, _ in component)
            left = min(col for _, col in component)
            right = max(col for _, col in component)
            shape = (bottom - top + 1, right - left + 1)
            if len(component) != shape[0] * shape[1]:
                valid = False
                break
            boxes.append((top, bottom, left, right))
            shapes.add(shape)
        if valid and len(shapes) == 1:
            candidates.append((color, shapes.pop(), boxes))
    if len(candidates) != 1:
        return [row[:] for row in grid]
    placeholder, shape, boxes = candidates[0]
    cells = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] != 0 and grid[row][col] != placeholder
    ]
    if not cells:
        return [row[:] for row in grid]
    top = min(row for row, _ in cells)
    bottom = max(row for row, _ in cells)
    left = min(col for _, col in cells)
    right = max(col for _, col in cells)
    if (bottom - top + 1, right - left + 1) != shape:
        return [row[:] for row in grid]
    template = [row[left : right + 1] for row in grid[top : bottom + 1]]
    output = [row[:] for row in grid]
    for box_top, box_bottom, box_left, box_right in boxes:
        for row in range(box_top, box_bottom + 1):
            output[row][box_left : box_right + 1] = template[row - box_top][:]
    return output
