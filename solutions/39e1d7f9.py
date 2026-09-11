def solve(grid):
    if not grid or not grid[0]:
        return grid
    height, width = len(grid), len(grid[0])
    separators = set()
    for row in grid:
        if row[0] and all(value == row[0] for value in row):
            separators.add(row[0])
    for col in range(width):
        if grid[0][col] and all(grid[row][col] == grid[0][col] for row in range(height)):
            separators.add(grid[0][col])
    if len(separators) != 1:
        return [row[:] for row in grid]
    separator = separators.pop()
    separator_rows = {
        row for row in range(height) if all(value == separator for value in grid[row])
    }
    separator_cols = {
        col for col in range(width) if all(grid[row][col] == separator for row in range(height))
    }
    row_groups = []
    start = 0
    for position in sorted(separator_rows):
        if start < position:
            row_groups.append((start, position))
        start = position + 1
    if start < height:
        row_groups.append((start, height))
    col_groups = []
    start = 0
    for position in sorted(separator_cols):
        if start < position:
            col_groups.append((start, position))
        start = position + 1
    if start < width:
        col_groups.append((start, width))
    if not row_groups or not col_groups:
        return [row[:] for row in grid]
    if len({bottom - top for top, bottom in row_groups}) != 1:
        return [row[:] for row in grid]
    if len({right - left for left, right in col_groups}) != 1:
        return [row[:] for row in grid]
    panels = {}
    for panel_row, (top, bottom) in enumerate(row_groups):
        for panel_col, (left, right) in enumerate(col_groups):
            values = {grid[row][col] for row in range(top, bottom) for col in range(left, right)}
            if not values or values == {0}:
                panels[panel_row, panel_col] = 0
            elif len(values) == 1:
                panels[panel_row, panel_col] = values.pop()
            else:
                return [row[:] for row in grid]
    best = None
    best_score = None
    colors = sorted({value for value in panels.values() if value not in (0, separator)})
    for center_color in colors:
        for center, value in panels.items():
            if value != center_color:
                continue
            offsets = {}
            orthogonal_count = 0
            for row_offset in (-1, 0, 1):
                for col_offset in (-1, 0, 1):
                    if not row_offset and not col_offset:
                        continue
                    position = center[0] + row_offset, center[1] + col_offset
                    value = panels.get(position, 0)
                    if value not in (0, center_color):
                        offsets[row_offset, col_offset] = value
                        orthogonal_count += not row_offset or not col_offset
            if len(offsets) < 2:
                continue
            score = len(offsets), orthogonal_count
            if best is None or score > best_score:
                best = center_color, offsets
                best_score = score
    if best is None:
        return [row[:] for row in grid]
    center_color, offsets = best
    output = [row[:] for row in grid]
    for center, value in panels.items():
        if value != center_color:
            continue
        for (row_offset, col_offset), paint_color in offsets.items():
            panel = center[0] + row_offset, center[1] + col_offset
            if not (0 <= panel[0] < len(row_groups) and 0 <= panel[1] < len(col_groups)):
                continue
            if panels.get(panel, 0) != 0:
                continue
            top, bottom = row_groups[panel[0]]
            left, right = col_groups[panel[1]]
            for row in range(top, bottom):
                output[row][left:right] = [paint_color] * (right - left)
    return output
