def solve(grid):
    height, width = len(grid), len(grid[0])
    row_candidates = [r for r in range(height) if len(set(grid[r])) == 1 and grid[r][0] != 0]
    col_candidates = [
        c for c in range(width) if len({grid[r][c] for r in range(height)}) == 1 and grid[0][c] != 0
    ]
    if len(row_candidates) < 2 or len(col_candidates) < 2:
        return [row[:] for row in grid]
    divider_colors = {grid[r][0] for r in row_candidates} & {grid[0][c] for c in col_candidates}
    if len(divider_colors) != 1:
        return [row[:] for row in grid]
    divider = next(iter(divider_colors))
    row_separators = [r for r in row_candidates if grid[r][0] == divider]
    col_separators = [c for c in col_candidates if grid[0][c] == divider]
    row_edges, col_edges = [-1, *row_separators, height], [-1, *col_separators, width]
    row_segments = [(a + 1, b) for a, b in zip(row_edges, row_edges[1:]) if b > a + 1]
    col_segments = [(a + 1, b) for a, b in zip(col_edges, col_edges[1:]) if b > a + 1]
    if not row_segments or not col_segments:
        return [row[:] for row in grid]
    counts = {}
    for row in grid:
        for value in row:
            if value != divider:
                counts[value] = counts.get(value, 0) + 1
    if not counts:
        return [row[:] for row in grid]
    background = max(counts, key=counts.get)
    markers = {}
    for cell_row, (top, bottom) in enumerate(row_segments):
        for cell_col, (left, right) in enumerate(col_segments):
            positions = [
                (r, c)
                for r in range(top, bottom)
                for c in range(left, right)
                if grid[r][c] not in (background, divider)
            ]
            if len(positions) > 1:
                return [row[:] for row in grid]
            if positions:
                r, c = positions[0]
                markers.setdefault(grid[r][c], set()).add((cell_row, cell_col))
    if not markers:
        return [row[:] for row in grid]
    coverage = {}
    for color, locations in markers.items():
        by_row, by_col = {}, {}
        for r, c in locations:
            by_row.setdefault(r, []).append(c)
            by_col.setdefault(c, []).append(r)
        for r, cols in by_row.items():
            if len(cols) >= 2:
                for c in range(min(cols), max(cols) + 1):
                    coverage.setdefault((r, c), set()).add(color)
        for c, rows in by_col.items():
            if len(rows) >= 2:
                for r in range(min(rows), max(rows) + 1):
                    coverage.setdefault((r, c), set()).add(color)
    if not coverage:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for (cell_row, cell_col), colors in coverage.items():
        if cell_row >= len(row_segments) or cell_col >= len(col_segments):
            continue
        top, bottom = row_segments[cell_row]
        left, right = col_segments[cell_col]
        fill = 6 if len(colors) > 1 else next(iter(colors))
        for r in range(top, bottom):
            for c in range(left, right):
                output[r][c] = fill
    return output
