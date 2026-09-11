def solve(grid):
    h, w = len(grid), len(grid[0])
    components = []
    for color in sorted({value for row in grid for value in row if value}):
        seen = set()
        for r in range(h):
            for c in range(w):
                if grid[r][c] != color or (r, c) in seen:
                    continue
                stack = [(r, c)]
                seen.add((r, c))
                cells = []
                while stack:
                    cr, cc = stack.pop()
                    cells.append((cr, cc))
                    for nr, nc in ((cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)):
                        if (
                            0 <= nr < h
                            and 0 <= nc < w
                            and grid[nr][nc] == color
                            and (nr, nc) not in seen
                        ):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
                components.append((color, cells))
    large = [item for item in components if len(item[1]) >= 8]
    if len(large) != 1:
        return [row[:] for row in grid]
    source_color, fan = large[0]
    top, bottom = min(r for r, _ in fan), max(r for r, _ in fan)
    left, right = min(c for _, c in fan), max(c for _, c in fan)
    marker_options = [
        (color, cells)
        for color, cells in components
        if color != source_color and len(cells) == 1 and cells[0][0] > bottom
    ]
    marker_colors = {color for color, _ in marker_options}
    if len(marker_colors) != 1:
        return [row[:] for row in grid]
    marker_color = next(iter(marker_colors))
    marker_columns = {
        col
        for color, [(row, col)] in marker_options
        if color == marker_color and left <= col <= right
    }
    if not marker_columns:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for col in marker_columns:
        source_rows = [row for row, fan_col in fan if fan_col == col]
        start = max(source_rows, default=top - 1) + 1
        for row in range(start, h):
            if output[row][col] == 0:
                output[row][col] = marker_color
    return output
