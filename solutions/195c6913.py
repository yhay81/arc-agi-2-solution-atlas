def _components(grid):
    height, width = len(grid), len(grid[0])
    by_color = {}
    for color in sorted({value for row in grid for value in row}):
        remaining = {
            (row, col) for row in range(height) for col in range(width) if grid[row][col] == color
        }
        parts = []
        while remaining:
            start = min(remaining)
            remaining.remove(start)
            stack = [start]
            component = []
            while stack:
                row, col = stack.pop()
                component.append((row, col))
                for point in (
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ):
                    if point in remaining:
                        remaining.remove(point)
                        stack.append(point)
            parts.append(component)
        by_color[color] = parts
    return by_color


def _find_palette(components):
    palette = []
    for color, parts in components.items():
        for cells in parts:
            rows = [row for row, _ in cells]
            cols = [col for _, col in cells]
            if (
                len(cells) == 4
                and max(rows) - min(rows) == max(cols) - min(cols) == 1
                and min(rows) <= 2
            ):
                palette.append((min(cols), color, cells))
    return sorted(palette)


def _paint_anchor(output, pattern, cap_color, row, boundary, start):
    for col in range(boundary):
        output[row][col] = pattern[(start + col) % len(pattern)]
    if cap_color is not None and boundary < len(output[0]):
        output[row][boundary] = cap_color


def _paint_vertical(grid, output, pattern, fill_color, cap_color, row, col, direction, index):
    traversed = []
    while 0 <= row < len(grid) and grid[row][col] == fill_color:
        output[row][col] = pattern[index]
        traversed.append((row, index))
        row += direction
        index = (index - direction) % len(pattern)
    if traversed and cap_color is not None and 0 <= row < len(grid):
        output[row][col] = cap_color
    return traversed


def _propagate(grid, output, pattern, fill_color, cap_color, anchor, direction):
    anchor_row, boundary, start = anchor
    left_col = boundary - 1
    anchor_index = (start + left_col) % len(pattern)
    traversed = _paint_vertical(
        grid,
        output,
        pattern,
        fill_color,
        cap_color,
        anchor_row + direction,
        left_col,
        direction,
        (anchor_index - direction) % len(pattern),
    )
    if not traversed:
        return

    boundary_row, boundary_index = traversed[-1]
    right = left_col
    while right < len(grid[0]) and grid[boundary_row][right] == fill_color:
        output[boundary_row][right] = pattern[(boundary_index + right - left_col) % len(pattern)]
        right += 1
    if cap_color is not None and right < len(grid[0]):
        output[boundary_row][right] = cap_color

    right_col = right - 1
    right_index = (boundary_index + right - left_col - 1) % len(pattern)
    traversed = _paint_vertical(
        grid,
        output,
        pattern,
        fill_color,
        cap_color,
        boundary_row + direction,
        right_col,
        direction,
        (right_index - direction) % len(pattern),
    )
    if not traversed:
        return

    row, index = traversed[-1]
    neighbor = row + direction
    if not 0 <= neighbor < len(grid) or grid[neighbor][right_col] == fill_color:
        return
    col = right_col + 1
    index = (index + 1) % len(pattern)
    while col < len(grid[0]) and grid[row][col] == fill_color:
        output[row][col] = pattern[index]
        index = (index + 1) % len(pattern)
        col += 1
    if cap_color is not None and col < len(grid[0]):
        output[row][col] = cap_color


def solve(grid):
    background = grid[0][0]
    components = _components(grid)
    palette = _find_palette(components)
    if not palette:
        return [row[:] for row in grid]
    pattern = [color for _, color, _ in palette]

    candidates = [
        (sum(row.count(color) for row in grid), color)
        for color in components
        if color != background and color not in pattern
    ]
    if not candidates:
        return [row[:] for row in grid]
    _, fill_color = max(candidates)
    remaining = [item for item in candidates if item[1] != fill_color]
    cap_color = min(remaining)[1] if remaining else None

    output = [row[:] for row in grid]
    for _, _, cells in palette:
        for row, col in cells:
            output[row][col] = background
    if cap_color is not None:
        for row, col in min(components[cap_color], key=len):
            output[row][col] = background

    anchors = []
    for row, values in enumerate(grid):
        if values[0] in pattern:
            boundary = next(
                (col for col in range(1, len(values)) if values[col] != fill_color),
                len(values),
            )
            if boundary > 1:
                anchors.append((row, boundary, pattern.index(values[0])))
    for anchor in sorted(anchors):
        _paint_anchor(output, pattern, cap_color, *anchor)
        _propagate(grid, output, pattern, fill_color, cap_color, anchor, -1)
        if len(anchors) == 1:
            _propagate(grid, output, pattern, fill_color, cap_color, anchor, 1)
    return output
