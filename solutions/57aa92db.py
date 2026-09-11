def solve(grid):
    height, width = len(grid), len(grid[0]) if grid else 0
    source = [row[:] for row in grid]
    output = [row[:] for row in source]
    occupied = {(row, col) for row in range(height) for col in range(width) if source[row][col]}
    components = []
    unseen = set(occupied)
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        stack = [start]
        component = []
        while stack:
            row, col = stack.pop()
            component.append((row, col))
            for next_row, next_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if (next_row, next_col) in unseen:
                    unseen.remove((next_row, next_col))
                    stack.append((next_row, next_col))
        components.append(component)
    candidates = []
    for component in components:
        colors = {source[row][col] for row, col in component}
        rows = [row for row, _ in component]
        cols = [col for _, col in component]
        if (
            len(colors) == 2
            and len(component) <= 10
            and max(rows) - min(rows) < 4
            and max(cols) - min(cols) < 4
        ):
            counts = sorted(
                sum(source[row][col] == color for row, col in component) for color in colors
            )
            candidates.append((counts[-1] - counts[0], component))
    if not candidates:
        return output
    _, template = max(candidates, key=lambda item: item[0])
    template_set = set(template)
    template_colors = {source[row][col] for row, col in template}
    color_counts = {
        color: sum(source[row][col] == color for row, col in template) for color in template_colors
    }
    marker_color = min(template_colors, key=lambda color: color_counts[color])
    dominant_color = next(color for color in template_colors if color != marker_color)
    top = min(row for row, _ in template)
    left = min(col for _, col in template)
    bottom = max(row for row, _ in template)
    right = max(col for _, col in template)
    marker_pattern = [
        (row - top, col - left) for row, col in template if source[row][col] == marker_color
    ]
    marker_cells = {(row, col) for row, col in occupied if source[row][col] == marker_color}
    marker_components = []
    unseen = set(marker_cells)
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        stack = [start]
        component = []
        while stack:
            row, col = stack.pop()
            component.append((row, col))
            for next_row, next_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if (next_row, next_col) in unseen:
                    unseen.remove((next_row, next_col))
                    stack.append((next_row, next_col))
        marker_components.append(component)
    for marker_component in marker_components:
        if set(marker_component) <= template_set:
            continue
        marker_rows = [row for row, _ in marker_component]
        marker_cols = [col for _, col in marker_component]
        scale = round(len(marker_component) ** 0.5)
        if (
            scale < 1
            or scale * scale != len(marker_component)
            or len(set(marker_rows)) != scale
            or len(set(marker_cols)) != scale
        ):
            scale = 1
        other_cells = [
            (row, col, source[row][col])
            for row in range(height)
            for col in range(width)
            if source[row][col]
            and source[row][col] not in (dominant_color, marker_color)
            and (row, col) not in template_set
        ]
        if not other_cells:
            continue
        center_row = sum(marker_rows) / len(marker_rows)
        center_col = sum(marker_cols) / len(marker_cols)
        _, _, seed_color = min(
            other_cells, key=lambda cell: abs(cell[0] - center_row) + abs(cell[1] - center_col)
        )
        for marker_row, marker_col in marker_pattern:
            render_top = min(marker_rows) - marker_row * scale
            render_left = min(marker_cols) - marker_col * scale
            render_height = (bottom - top + 1) * scale
            render_width = (right - left + 1) * scale
            if (
                render_top < 0
                or render_left < 0
                or render_top + render_height > height
                or render_left + render_width > width
            ):
                continue
            for row_offset in range(bottom - top + 1):
                for col_offset in range(right - left + 1):
                    value = source[top + row_offset][left + col_offset]
                    if value not in (dominant_color, marker_color):
                        continue
                    fill = seed_color if value == dominant_color else marker_color
                    for row in range(
                        render_top + row_offset * scale, render_top + (row_offset + 1) * scale
                    ):
                        for col in range(
                            render_left + col_offset * scale, render_left + (col_offset + 1) * scale
                        ):
                            output[row][col] = fill
    return output
