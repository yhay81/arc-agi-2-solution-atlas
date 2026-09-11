def solve(grid):
    height, width = len(grid), len(grid[0])
    components = {2: [], 3: []}
    for color in components:
        seen = set()
        for row in range(height):
            for col in range(width):
                if grid[row][col] != color or (row, col) in seen:
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
                            and grid[next_row][next_col] == color
                            and (next_row, next_col) not in seen
                        ):
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
                components[color].append(component)
    if any(len(components[color]) != 1 or len(components[color][0]) != 2 for color in components):
        return [row[:] for row in grid]
    source = set(components[3][0])
    target = set(components[2][0])
    source_rows = {row for row, _ in source}
    source_cols = {col for _, col in source}
    target_rows = {row for row, _ in target}
    target_cols = {col for _, col in target}
    if len(source_rows) == len(source_cols):
        return [row[:] for row in grid]
    values = sorted({value for row in grid for value in row})
    background = max(values, key=lambda value: sum(row.count(value) for row in grid))
    source_row = sum((row for row, _ in source)) / 2
    source_col = sum((col for _, col in source)) / 2
    target_row = sum((row for row, _ in target)) / 2
    target_col = sum((col for _, col in target)) / 2
    vertical = len(source_rows) == 2
    path: list[tuple[int, int]] = []
    if vertical:
        along = 1 if target_row > source_row else -1
        row = max(source_rows) if along > 0 else min(source_rows)
        col = next(iter(source_cols))
        while 0 <= row + along < height and grid[row + along][col] == background:
            row += along
            path.append((row, col))
        across = 1 if target_col > col else -1
        while col != int(target_col):
            col += across
            path.append((row, col))
        target_edge = min(target_rows) if along > 0 else max(target_rows)
        endpoint = target_edge - along
        while row != endpoint:
            row += along
            path.append((row, col))
    else:
        along = 1 if source_col < (width - 1) / 2 else -1
        row = next(iter(source_rows))
        col = max(source_cols) if along > 0 else min(source_cols)
        while 0 <= col + along < width and grid[row][col + along] == background:
            col += along
            path.append((row, col))
        across = 1 if target_row > row else -1
        while row != int(target_row):
            row += across
            path.append((row, col))
        target_edge = max(target_cols) if along > 0 else min(target_cols)
        endpoint = target_edge + 1 if along > 0 else target_edge - 1
        while col != endpoint:
            col -= along
            path.append((row, col))
    output = [row[:] for row in grid]
    for row, col in path:
        if output[row][col] == background:
            output[row][col] = 3
    return output
