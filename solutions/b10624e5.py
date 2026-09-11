def solve(grid):
    grid = [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    row_axis = max(range(height), key=lambda r: sum(grid[r][c] == 1 for c in range(width)))
    col_axis = max(range(width), key=lambda c: sum(grid[r][c] == 1 for r in range(height)))
    unseen = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == 2}
    parts = []
    while unseen:
        start = unseen.pop()
        stack, cells = [start], [start]
        while stack:
            r, c = stack.pop()
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in unseen:
                    unseen.remove(point)
                    cells.append(point)
                    stack.append(point)
        top, bottom = min(r for r, _ in cells), max(r for r, _ in cells)
        left, right = min(c for _, c in cells), max(c for _, c in cells)
        rows = range(row_axis) if top < row_axis else range(row_axis + 1, height)
        cols = range(col_axis) if left < col_axis else range(col_axis + 1, width)
        pattern = [(r, c) for r in rows for c in cols if grid[r][c] != 4]
        parts.append((len(pattern) - len(cells), cells, pattern))
    _, source, pattern = max(parts, key=lambda part: part[0])
    sr, sb = min(r for r, _ in source), max(r for r, _ in source)
    sc, sd = min(c for _, c in source), max(c for _, c in source)
    source_height, source_width = sb - sr + 1, sd - sc + 1
    for _, cells, _ in parts:
        top, bottom = min(r for r, _ in cells), max(r for r, _ in cells)
        left, right = min(c for _, c in cells), max(c for _, c in cells)
        height_scale = (bottom - top + 1) / source_height
        width_scale = (right - left + 1) / source_width
        flip_row = (top < row_axis) != (sr < row_axis)
        flip_col = (left < col_axis) != (sc < col_axis)
        for row, col in pattern:
            r0 = int((row - sr) * height_scale)
            r1 = int((row - sr + 1) * height_scale)
            c0 = int((col - sc) * width_scale)
            c1 = int((col - sc + 1) * width_scale)
            target_rows = (
                range(bottom + 1 - r1, bottom + 1 - r0) if flip_row else range(top + r0, top + r1)
            )
            target_cols = (
                range(right + 1 - c1, right + 1 - c0) if flip_col else range(left + c0, left + c1)
            )
            for target_row in target_rows:
                for target_col in target_cols:
                    if 0 <= target_row < height and 0 <= target_col < width:
                        grid[target_row][target_col] = grid[row][col]
    return grid
