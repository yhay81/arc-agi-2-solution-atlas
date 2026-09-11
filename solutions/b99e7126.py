def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    row_separators = [
        row for row in range(height) if len(set(grid[row])) == 1 and grid[row][0] != 0
    ]
    col_separators = [
        col
        for col in range(width)
        if len({grid[row][col] for row in range(height)}) == 1 and grid[0][col] != 0
    ]
    if len(row_separators) < 2 or len(col_separators) < 2:
        return output
    row_intervals = [
        (start + 1, stop)
        for start, stop in zip(row_separators, row_separators[1:])
        if stop > start + 1
    ]
    col_intervals = [
        (start + 1, stop)
        for start, stop in zip(col_separators, col_separators[1:])
        if stop > start + 1
    ]
    if not row_intervals or not col_intervals:
        return output
    cells = []
    for cell_row, (top, bottom) in enumerate(row_intervals):
        for cell_col, (left, right) in enumerate(col_intervals):
            tile = tuple(tuple(grid[row][left:right]) for row in range(top, bottom))
            cells.append(((cell_row, cell_col), tile))
    if not cells:
        return output
    shapes = {(len(tile), len(tile[0])) for _, tile in cells}
    if len(shapes) != 1:
        return output
    counts = {}
    patterns = {}
    for _, tile in cells:
        key = tuple(value for row in tile for value in row)
        counts[key] = counts.get(key, 0) + 1
        patterns[key] = tile
    if len(counts) < 2:
        return output
    baseline_key = max(counts, key=counts.get)
    baseline = patterns[baseline_key]
    baseline_colors = {value for row in baseline for value in row}
    candidates = []
    for key, count in counts.items():
        if key == baseline_key:
            continue
        tile = patterns[key]
        introduced = {value for row in tile for value in row} - baseline_colors
        if len(introduced) != 1:
            continue
        marker = next(iter(introduced))
        mask = {
            (row, col)
            for row, values in enumerate(tile)
            for col, value in enumerate(values)
            if value == marker
        }
        if mask:
            candidates.append((tile, mask, count))
    if not candidates:
        return output
    best_count = min(item[2] for item in candidates)
    selected = [item for item in candidates if item[2] == best_count]
    if len(selected) != 1:
        return output
    template, mask, _ = selected[0]
    marked_positions = {position for position, tile in cells if tile == template}
    if not marked_positions:
        return output
    anchors = set()
    for marked_row, marked_col in marked_positions:
        for mask_row, mask_col in mask:
            anchor = (marked_row - mask_row, marked_col - mask_col)
            translated = {(anchor[0] + row, anchor[1] + col) for row, col in mask}
            if marked_positions <= translated and all(
                (
                    0 <= row < len(row_intervals) and 0 <= col < len(col_intervals)
                    for row, col in translated
                )
            ):
                anchors.add(anchor)
    if len(anchors) != 1:
        return output
    anchor = next(iter(anchors))
    for cell_row, cell_col in {(anchor[0] + row, anchor[1] + col) for row, col in mask}:
        top, bottom = row_intervals[cell_row]
        left, right = col_intervals[cell_col]
        for row, values in enumerate(template, top):
            output[row][left:right] = values
    return output
