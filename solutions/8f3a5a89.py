def solve(grid):
    height, width = len(grid), len(grid[0])
    background, obj, outline, marker = 8, 1, 7, 6
    source = [row[:] for row in grid]
    markers = [
        (row, col) for row in range(height) for col in range(width) if source[row][col] == marker
    ]
    if len(markers) != 1:
        return source
    marker_position = markers[0]
    reachable = {marker_position}
    stack = [marker_position]
    while stack:
        row, col = stack.pop()
        for drow, dcol in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_row, next_col = row + drow, col + dcol
            if (
                0 <= next_row < height
                and 0 <= next_col < width
                and (next_row, next_col) not in reachable
                and source[next_row][next_col] == background
            ):
                reachable.add((next_row, next_col))
                stack.append((next_row, next_col))
    objects = []
    seen = set()
    for row in range(height):
        for col in range(width):
            if source[row][col] != obj or (row, col) in seen:
                continue
            component = [(row, col)]
            seen.add((row, col))
            stack = [(row, col)]
            while stack:
                current_row, current_col = stack.pop()
                for drow, dcol in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_row, next_col = current_row + drow, current_col + dcol
                    if (
                        0 <= next_row < height
                        and 0 <= next_col < width
                        and (next_row, next_col) not in seen
                        and source[next_row][next_col] == obj
                    ):
                        seen.add((next_row, next_col))
                        component.append((next_row, next_col))
                        stack.append((next_row, next_col))
            objects.append(component)
    retained = set()
    edge_objects = set()
    for component in objects:
        if any(
            (row + drow, col + dcol) in reachable
            for row, col in component
            for drow in (-1, 0, 1)
            for dcol in (-1, 0, 1)
            if (drow, dcol) != (0, 0)
        ):
            retained.update(component)
        if any(row in (0, height - 1) or col in (0, width - 1) for row, col in component):
            edge_objects.update(component)
    output = [[background] * width for _ in range(height)]
    output[marker_position[0]][marker_position[1]] = marker
    for row, col in retained:
        output[row][col] = obj
    for row, col in reachable:
        if source[row][col] != background:
            continue
        near_edge_object = any(
            (row + drow, col + dcol) in edge_objects
            for drow in (-1, 0, 1)
            for dcol in (-1, 0, 1)
            if (drow, dcol) != (0, 0)
        )
        if row in (0, height - 1) or col in (0, width - 1) or near_edge_object:
            output[row][col] = outline
    return output
