def solve(grid):
    source = [list(row) for row in grid]
    if not source or not source[0]:
        return source
    height, width = len(source), len(source[0])
    counts = {}
    for row in source:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = min(((-count, value) for value, count in counts.items()))[1]
    components = []
    for color in counts:
        if color == background:
            continue
        seen = set()
        for row in range(height):
            for col in range(width):
                if source[row][col] != color or (row, col) in seen:
                    continue
                stack = [(row, col)]
                seen.add((row, col))
                cells = []
                while stack:
                    current_row, current_col = stack.pop()
                    cells.append((current_row, current_col))
                    for next_row in range(current_row - 1, current_row + 2):
                        for next_col in range(current_col - 1, current_col + 2):
                            if (
                                0 <= next_row < height
                                and 0 <= next_col < width
                                and source[next_row][next_col] == color
                                and (next_row, next_col) not in seen
                            ):
                                seen.add((next_row, next_col))
                                stack.append((next_row, next_col))
                components.append((color, cells))
    templates = [item for item in components if len(item[1]) > 1]
    if len(templates) != 1:
        return source
    template_color, template = templates[0]
    markers = [item for item in components if item[0] != template_color and len(item[1]) == 1]
    if len(markers) != 1:
        return source
    marker_color, [(marker_row, marker_col)] = markers[0]
    top = min(row for row, _ in template)
    left = min(col for _, col in template)
    template_height = max(row for row, _ in template) - top + 1
    template_width = max(col for _, col in template) - left + 1
    center_row = top + template_height // 2
    center_col = left + template_width // 2
    row_direction = (marker_row > center_row) - (marker_row < center_row)
    col_direction = (marker_col > center_col) - (marker_col < center_col)
    candidates = template
    if row_direction:
        row_edge = (
            min(row for row, _ in candidates)
            if row_direction > 0
            else max(row for row, _ in candidates)
        )
        candidates = [point for point in candidates if point[0] == row_edge]
    if col_direction:
        col_edge = (
            max(col for _, col in candidates)
            if col_direction < 0
            else min(col for _, col in candidates)
        )
        candidates = [point for point in candidates if point[1] == col_edge]
    if len(candidates) != 1:
        return source
    step_row = marker_row - candidates[0][0]
    step_col = marker_col - candidates[0][1]
    if not (step_row or step_col):
        return source
    offsets = [(row - top, col - left) for row, col in template]
    output = [row[:] for row in source]
    tile_top, tile_left = top + step_row, left + step_col
    while (
        tile_top < height
        and tile_left < width
        and tile_top + template_height > 0
        and tile_left + template_width > 0
    ):
        for row_offset, col_offset in offsets:
            row, col = tile_top + row_offset, tile_left + col_offset
            if 0 <= row < height and 0 <= col < width and output[row][col] == background:
                output[row][col] = marker_color
        tile_top += step_row
        tile_left += step_col
    return output
