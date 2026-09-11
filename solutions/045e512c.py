def solve(grid):
    height, width = len(grid), len(grid[0]) if grid else 0
    source = [row[:] for row in grid]
    components = []
    for color in sorted({value for row in source for value in row if value}):
        seen = set()
        for row in range(height):
            for col in range(width):
                if source[row][col] != color or (row, col) in seen:
                    continue
                seen.add((row, col))
                stack = [(row, col)]
                component = []
                while stack:
                    current_row, current_col = stack.pop()
                    component.append((current_row, current_col))
                    for row_delta in (-1, 0, 1):
                        for col_delta in (-1, 0, 1):
                            next_row = current_row + row_delta
                            next_col = current_col + col_delta
                            if (
                                0 <= next_row < height
                                and 0 <= next_col < width
                                and source[next_row][next_col] == color
                                and (next_row, next_col) not in seen
                            ):
                                seen.add((next_row, next_col))
                                stack.append((next_row, next_col))
                components.append(component)
    if len(components) < 2:
        return source
    boxes = []
    for component in components:
        rows = [row for row, _ in component]
        cols = [col for _, col in component]
        top, bottom = min(rows), max(rows)
        left, right = min(cols), max(cols)
        boxes.append((top, left, bottom - top + 1, right - left + 1, component))
    largest_area = max(height * width for _, _, height, width, _ in boxes)
    templates = [box for box in boxes if box[2] * box[3] == largest_area]
    if len(templates) != 1:
        return source
    template_top, template_left, tile_height, tile_width, template_cells = templates[0]
    if tile_height < 2 or tile_width < 2 or len(template_cells) < 2:
        return source
    template_mask = {(row - template_top, col - template_left) for row, col in template_cells}
    template_index = boxes.index(templates[0])
    output = [row[:] for row in source]
    found_marker = False
    for box_index, (_, _, _, _, marker_cells) in enumerate(boxes):
        if box_index == template_index:
            continue
        directions = []
        for row_delta in (-1, 0, 1):
            for col_delta in (-1, 0, 1):
                if (row_delta, col_delta) == (0, 0):
                    continue
                top = template_top + row_delta * (tile_height + 1)
                left = template_left + col_delta * (tile_width + 1)
                if not (
                    top < height
                    and left < width
                    and top + tile_height > 0
                    and left + tile_width > 0
                ):
                    continue
                if all(
                    top <= row < top + tile_height
                    and left <= col < left + tile_width
                    and (row - top, col - left) in template_mask
                    for row, col in marker_cells
                ):
                    directions.append((row_delta, col_delta))
        if len(directions) != 1:
            continue
        found_marker = True
        row_delta, col_delta = directions[0]
        top = template_top + row_delta * (tile_height + 1)
        left = template_left + col_delta * (tile_width + 1)
        marker_color = source[marker_cells[0][0]][marker_cells[0][1]]
        while top < height and left < width and top + tile_height > 0 and left + tile_width > 0:
            for row_offset, col_offset in template_mask:
                row, col = top + row_offset, left + col_offset
                if 0 <= row < height and 0 <= col < width and output[row][col] == 0:
                    output[row][col] = marker_color
            top += row_delta * (tile_height + 1)
            left += col_delta * (tile_width + 1)
    return output if found_marker else source
