def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    template = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 8]
    markers = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 2]
    if not template or not markers:
        return output
    template_rows, template_cols = {r for r, _ in template}, {c for _, c in template}
    marker_rows, marker_cols = sorted({r for r, _ in markers}), sorted({c for _, c in markers})
    if len(template_rows) == 1 and len(marker_cols) == 1:
        direction = -1 if marker_cols[0] > width // 2 else 1
        for row in range(height):
            shift = direction * sum(marker_row <= row for marker_row in marker_rows)
            for _, col in template:
                target = col + shift
                if 0 <= target < width and not output[row][target]:
                    output[row][target] = 8
    elif len(template_cols) == 1 and len(marker_rows) == 1:
        source_col = next(iter(template_cols))
        direction = -1 if marker_rows[0] > height // 2 else 1
        for col in range(width):
            shift = (
                sum(marker_col <= col for marker_col in marker_cols)
                if source_col < marker_cols[0]
                else sum(marker_col >= col for marker_col in marker_cols)
            )
            shift *= direction
            for row, _ in template:
                target = row + shift
                if 0 <= target < height and not output[target][col]:
                    output[target][col] = 8
    return output
