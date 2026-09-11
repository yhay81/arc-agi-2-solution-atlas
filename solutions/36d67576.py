def solve(grid):
    height, width = len(grid), len(grid[0]) if grid else 0
    source = [row[:] for row in grid]
    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if source[row][col] != 4 or (row, col) in seen:
                continue
            seen.add((row, col))
            stack = [(row, col)]
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
                        and source[next_row][next_col] == 4
                        and (next_row, next_col) not in seen
                    ):
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))
            top, bottom = min(row for row, _ in component), max(row for row, _ in component)
            left, right = min(col for _, col in component), max(col for _, col in component)
            markers = [
                (row, col, source[row][col])
                for row in range(max(0, top - 1), min(height, bottom + 2))
                for col in range(max(0, left - 1), min(width, right + 2))
                if source[row][col] not in (0, 4)
            ]
            components.append((component, markers, top, left, right - left + 1))
    if len(components) < 2:
        return source
    source_component, markers, source_top, source_left, source_width = max(
        components, key=lambda item: (len(item[1]), len({value for _, _, value in item[1]}))
    )
    output = [row[:] for row in source]
    source_shape = set(source_component)
    for target_component, _, target_top, target_left, _ in components:
        if target_component is source_component:
            continue
        target_shape = set(target_component)
        target_bottom = max(row for row, _ in target_component)
        target_right = max(col for _, col in target_component)
        candidates = []
        for reflection in (False, True):
            for rotations in range(4):
                shape_points = []
                for row, col in source_component:
                    row -= source_top
                    col -= source_left
                    if reflection:
                        col = source_width - 1 - col
                    for _ in range(rotations):
                        row, col = col, -row
                    shape_points.append((row, col))
                minimum_row = min(row for row, _ in shape_points)
                minimum_col = min(col for _, col in shape_points)
                shape = {
                    (row - minimum_row + target_top, col - minimum_col + target_left)
                    for row, col in shape_points
                }
                if shape != target_shape:
                    continue
                labels = []
                for row, col, value in markers:
                    row -= source_top
                    col -= source_left
                    if reflection:
                        col = source_width - 1 - col
                    for _ in range(rotations):
                        row, col = col, -row
                    labels.append(
                        (row - minimum_row + target_top, col - minimum_col + target_left, value)
                    )
                conflicts = 0
                matches = 0
                for row, col, value in labels:
                    if not (0 <= row < height and 0 <= col < width):
                        conflicts += 1
                    elif source[row][col] == value:
                        matches += 1
                    elif source[row][col] != 0:
                        conflicts += 1
                candidates.append((conflicts, -matches, int(reflection), rotations, labels))
        if not candidates:
            continue
        candidates.sort(key=lambda candidate: candidate[:4])
        conflicts, _, _, _, labels = candidates[0]
        if conflicts:
            continue
        for row, col, value in labels:
            if 0 <= row < height and 0 <= col < width and output[row][col] == 0:
                output[row][col] = value
    return output
