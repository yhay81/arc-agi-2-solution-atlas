def solve(grid):
    height, width = len(grid), len(grid[0])
    separator_colors = set()
    for row in grid:
        if row[0] and all(value == row[0] for value in row):
            separator_colors.add(row[0])
    for col in range(width):
        if grid[0][col] and all(grid[row][col] == grid[0][col] for row in range(height)):
            separator_colors.add(grid[0][col])
    if len(separator_colors) != 1:
        return [row[:] for row in grid]
    separator = separator_colors.pop()
    separator_rows = {r for r, row in enumerate(grid) if all(value == separator for value in row)}
    separator_cols = {
        c for c in range(width) if all(grid[r][c] == separator for r in range(height))
    }
    row_groups, start = [], 0
    for cut in sorted(separator_rows):
        if start < cut:
            row_groups.append((start, cut))
        start = cut + 1
    if start < height:
        row_groups.append((start, height))
    col_groups, start = [], 0
    for cut in sorted(separator_cols):
        if start < cut:
            col_groups.append((start, cut))
        start = cut + 1
    if start < width:
        col_groups.append((start, width))
    panels = [
        (top, bottom, left, right) for top, bottom in row_groups for left, right in col_groups
    ]
    shapes = {(bottom - top, right - left) for top, bottom, left, right in panels}
    if len(panels) < 2 or len(shapes) != 1:
        return [row[:] for row in grid]
    nonempty = [
        panel
        for panel in panels
        if any(grid[r][c] for r in range(panel[0], panel[1]) for c in range(panel[2], panel[3]))
    ]
    if len(nonempty) != 1:
        return [row[:] for row in grid]
    top, bottom, left, right = nonempty[0]
    source = [grid[r][left:right] for r in range(top, bottom)]
    output = [row[:] for row in grid]
    for top, bottom, left, right in panels:
        for r, values in enumerate(source, top):
            output[r][left:right] = values[:]
    return output
