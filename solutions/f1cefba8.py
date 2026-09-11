def solve(grid):
    height, width = len(grid), len(grid[0])
    values = {value for row in grid for value in row}
    nonzero = [value for value in values if value != 0]
    if len(nonzero) != 2:
        return [row[:] for row in grid]
    framed = []
    for value in nonzero:
        points = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == value]
        top = min(r for r, _ in points)
        left = min(c for _, c in points)
        bottom = max(r for r, _ in points)
        right = max(c for _, c in points)
        if (
            bottom > top
            and right > left
            and all(grid[top][c] == value for c in range(left, right + 1))
            and all(grid[bottom][c] == value for c in range(left, right + 1))
            and all(grid[r][left] == value for r in range(top, bottom + 1))
            and all(grid[r][right] == value for r in range(top, bottom + 1))
        ):
            framed.append(value)
    base = (
        framed[0]
        if len(framed) == 1
        else max(nonzero, key=lambda value: sum(row.count(value) for row in grid))
    )
    marker = next(value for value in nonzero if value != base)
    base_points = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == base]
    if not base_points:
        return [row[:] for row in grid]
    top = min(r for r, _ in base_points)
    left = min(c for _, c in base_points)
    bottom = max(r for r, _ in base_points)
    right = max(c for _, c in base_points)
    marker_points = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == marker]
    if not marker_points:
        return [row[:] for row in grid]
    rows = {}
    for r, c in marker_points:
        rows.setdefault(r, []).append(c)
    min_row, max_row = min(rows), max(rows)
    widest = max(rows, key=lambda r: (len(rows[r]), -r))
    guide_cols = list(rows[min_row])
    if max_row != min_row and len(rows[max_row]) <= 2:
        guide_cols.extend(rows[max_row])
    if not guide_cols:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for r, c in marker_points:
        if r == widest or c in guide_cols:
            output[r][c] = base
    for c in sorted(set(guide_cols)):
        if 0 <= c < width:
            for r in range(top):
                output[r][c] = marker
            for r in range(bottom + 1, height):
                output[r][c] = marker
    for c in range(left):
        output[widest][c] = marker
    for c in range(right + 1, width):
        output[widest][c] = marker
    return output
