def solve(grid):
    h, w = len(grid), len(grid[0])
    separator_colors = set()
    for r in range(h):
        if grid[r][0] and len(set(grid[r])) == 1:
            separator_colors.add(grid[r][0])
    for c in range(w):
        if grid[0][c] and len({grid[r][c] for r in range(h)}) == 1:
            separator_colors.add(grid[0][c])
    if len(separator_colors) != 1:
        return [row[:] for row in grid]
    separator = separator_colors.pop()
    separator_rows = {r for r in range(h) if all(value == separator for value in grid[r])}
    separator_cols = {c for c in range(w) if all(grid[r][c] == separator for r in range(h))}

    def groups(length, separators):
        result, start = [], 0
        for position in sorted(separators):
            if start < position:
                result.append((start, position))
            start = position + 1
        if start < length:
            result.append((start, length))
        return result

    row_groups, col_groups = groups(h, separator_rows), groups(w, separator_cols)
    if (
        len(row_groups) != 3
        or len(col_groups) != 3
        or any((b - a, d - c) != (3, 3) for a, b in row_groups for c, d in col_groups)
    ):
        return [row[:] for row in grid]
    markers = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 4]
    if len(markers) != 1:
        return [row[:] for row in grid]
    marker_row, marker_col = markers[0]
    source_row = next((i for i, (a, b) in enumerate(row_groups) if a <= marker_row < b), -1)
    source_col = next((i for i, (a, b) in enumerate(col_groups) if a <= marker_col < b), -1)
    if source_row < 0 or source_col < 0:
        return [row[:] for row in grid]
    destination_row = marker_row - row_groups[source_row][0]
    destination_col = marker_col - col_groups[source_col][0]
    if destination_row >= len(row_groups) or destination_col >= len(col_groups):
        return [row[:] for row in grid]
    st, sb = row_groups[source_row]
    sl, sr = col_groups[source_col]
    source = [row[sl:sr] for row in grid[st:sb]]
    output = [[0] * w for _ in range(h)]
    for r in separator_rows:
        output[r] = [separator] * w
    for c in separator_cols:
        for r in range(h):
            output[r][c] = separator
    tt, tb = row_groups[destination_row]
    tl, tr = col_groups[destination_col]
    for r in range(3):
        output[tt + r][tl:tr] = source[r]
    return output
