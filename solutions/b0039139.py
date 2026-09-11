def solve(grid):
    height, width = len(grid), len(grid[0])
    source = [row[:] for row in grid]
    separator_rows = [row for row in range(height) if all(value == 1 for value in source[row])]
    separator_cols = [
        col for col in range(width) if all(source[row][col] == 1 for row in range(height))
    ]
    if bool(separator_rows) == bool(separator_cols):
        return source
    axis, separators = (0, separator_rows) if separator_rows else (1, separator_cols)
    edges = [-1, *separators, (height, width)[axis]]
    panels = []
    for start, stop in zip(edges, edges[1:]):
        if stop <= start + 1:
            continue
        if axis == 0:
            panels.append(source[start + 1 : stop])
        else:
            panels.append([row[start + 1 : stop] for row in source])
    if len(panels) != 4:
        return source
    glyph_values = {value for row in panels[0] for value in row if value}
    component_values = {value for row in panels[1] for value in row if value}
    if len(glyph_values) != 1 or len(component_values) != 1:
        return source
    if any(value != panels[2][0][0] for row in panels[2] for value in row):
        return source
    if any(value != panels[3][0][0] for row in panels[3] for value in row):
        return source
    glyph_color = next(iter(glyph_values))
    component_color = next(iter(component_values))
    glyph_cells = [
        (row, col)
        for row in range(len(panels[0]))
        for col in range(len(panels[0][0]))
        if panels[0][row][col] == glyph_color
    ]
    if not glyph_cells:
        return source
    top = min(row for row, _ in glyph_cells)
    bottom = max(row for row, _ in glyph_cells)
    left = min(col for _, col in glyph_cells)
    right = max(col for _, col in glyph_cells)
    glyph = [
        [panels[0][row][col] == glyph_color for col in range(left, right + 1)]
        for row in range(top, bottom + 1)
    ]
    component_cells = {
        (row, col)
        for row in range(len(panels[1]))
        for col in range(len(panels[1][0]))
        if panels[1][row][col] == component_color
    }
    components = 0
    while component_cells:
        stack = [component_cells.pop()]
        while stack:
            row, col = stack.pop()
            for next_cell in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if next_cell in component_cells:
                    component_cells.remove(next_cell)
                    stack.append(next_cell)
        components += 1
    if not components:
        return source
    gap_color = panels[3][0][0]
    output_color = panels[2][0][0]
    glyph_height, glyph_width = len(glyph), len(glyph[0])
    output_height = glyph_height * components + components - 1 if axis == 0 else glyph_height
    output_width = glyph_width if axis == 0 else glyph_width * components + components - 1
    output = [[gap_color for _ in range(output_width)] for _ in range(output_height)]
    for index in range(components):
        offset = index * (glyph_height + 1 if axis == 0 else glyph_width + 1)
        for row in range(glyph_height):
            for col in range(glyph_width):
                if glyph[row][col]:
                    target = (row + offset, col) if axis == 0 else (row, col + offset)
                    output[target[0]][target[1]] = output_color
    return output
