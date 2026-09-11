def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    output = [row[:] for row in grid]
    values = sorted({value for row in grid for value in row})
    if len(values) < 3:
        return output
    counts = {value: sum(row.count(value) for row in grid) for value in values}
    background = max(values, key=lambda value: counts[value])
    components = []
    for color in values:
        if color == background:
            continue
        remaining = {
            (row, col) for row in range(rows) for col in range(cols) if grid[row][col] == color
        }
        while remaining:
            start = remaining.pop()
            stack = [start]
            cells = [start]
            while stack:
                row, col = stack.pop()
                for next_row, next_col in (
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ):
                    point = (next_row, next_col)
                    if point in remaining:
                        remaining.remove(point)
                        stack.append(point)
                        cells.append(point)
            components.append((color, cells))
    if len(components) != 2:
        return output
    irregular = []
    for color, cells in components:
        top = min(row for row, _ in cells)
        bottom = max(row for row, _ in cells)
        left = min(col for _, col in cells)
        right = max(col for _, col in cells)
        rectangle = {(row, col) for row in range(top, bottom + 1) for col in range(left, right + 1)}
        if set(cells) != rectangle:
            irregular.append((color, cells))
    if len(irregular) != 1:
        return output
    target_color, target = irregular[0]
    reference = next(cells for color, cells in components if color != target_color)
    target_set = set(target)
    target_top = min(row for row, _ in target)
    target_bottom = max(row for row, _ in target)
    target_left = min(col for _, col in target)
    target_right = max(col for _, col in target)
    ref_row = sum(row for row, _ in reference) / len(reference)
    ref_col = sum(col for _, col in reference) / len(reference)
    best = None
    best_rect = (target_top, target_bottom, target_left, target_right)
    for top in range(target_top, target_bottom + 1):
        for bottom in range(top + 1, target_bottom + 1):
            for left in range(target_left, target_right + 1):
                for right in range(left + 1, target_right + 1):
                    cells = {
                        (row, col)
                        for row in range(top, bottom + 1)
                        for col in range(left, right + 1)
                    }
                    if not cells.issubset(target_set):
                        continue
                    distance = abs((top + bottom) / 2 - ref_row) + abs((left + right) / 2 - ref_col)
                    key = (len(cells), -int(distance * 1000), -top, -left, bottom, right)
                    if best is None or key > best:
                        best = key
                        best_rect = (top, bottom, left, right)
    if best is None:
        return output
    top, bottom, left, right = best_rect
    new_top, new_bottom, new_left, new_right = best_rect
    target_center = (
        (target_top + target_bottom) / 2,
        (target_left + target_right) / 2,
    )
    if abs(ref_row - target_center[0]) >= abs(ref_col - target_center[1]):
        if ref_row < target_center[0]:
            new_top = target_top
            new_bottom = target_top + bottom - top
        else:
            new_bottom = target_bottom
            new_top = target_bottom - (bottom - top)
    elif ref_col < target_center[1]:
        new_left = target_left
        new_right = target_left + right - left
    else:
        new_right = target_right
        new_left = target_right - (right - left)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == target_color:
                output[row][col] = background
    for row in range(new_top, new_bottom + 1):
        for col in range(new_left, new_right + 1):
            output[row][col] = target_color
    return output
