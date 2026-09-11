def solve(grid):
    height, width = len(grid), len(grid[0]) if grid else 0
    if not grid or min(height, width) < 3:
        return [row[:] for row in grid]
    values = sorted({cell for row in grid for cell in row})
    counts = {value: sum(cell == value for row in grid for cell in row) for value in values}
    background = max(values, key=lambda value: counts[value])
    separators = []
    for color in values:
        if color == background:
            continue
        for row in range(height):
            if all(grid[row][col] == color for col in range(width)) and counts[color] > width:
                separators.append((0, row, color))
        for col in range(width):
            if all(grid[row][col] == color for row in range(height)) and counts[color] > height:
                separators.append((1, col, color))
    if not separators:
        return [row[:] for row in grid]
    axis, separator, frame = max(
        separators,
        key=lambda item: counts[item[2]] - (width if item[0] == 0 else height),
    )
    if axis == 0:
        negative_extra = sum(cell == frame for row in grid[:separator] for cell in row)
        positive_extra = sum(cell == frame for row in grid[separator + 1 :] for cell in row)
    else:
        negative_extra = sum(
            grid[row][col] == frame for row in range(height) for col in range(separator)
        )
        positive_extra = sum(
            grid[row][col] == frame for row in range(height) for col in range(separator + 1, width)
        )
    if negative_extra == positive_extra:
        return [row[:] for row in grid]
    interior = -1 if negative_extra > positive_extra else 1
    exterior = -interior
    backgrounds = {}
    for side in (-1, 1):
        if axis == 0:
            region = grid[:separator] if side < 0 else grid[separator + 1 :]
            cells = [cell for row in region for cell in row if cell != frame]
        else:
            columns = range(separator) if side < 0 else range(separator + 1, width)
            cells = [
                grid[row][col]
                for row in range(height)
                for col in columns
                if grid[row][col] != frame
            ]
        if not cells:
            return [row[:] for row in grid]
        candidates = sorted(set(cells))
        backgrounds[side] = max(candidates, key=lambda value: cells.count(value))

    line_length = width if axis == 0 else height
    tracks = {}
    for side in (interior, exterior):
        positions = range(separator) if side < 0 else range(separator + 1, line_length)
        tracks[side] = []
        for position in positions:
            line = grid[position] if axis == 0 else [grid[row][position] for row in range(height)]
            active = {
                coordinate
                for coordinate, value in enumerate(line)
                if value not in (backgrounds[side], frame)
            }
            if len(active) >= 2 and len({line[coordinate] for coordinate in active}) >= 2:
                tracks[side].append((position, active))
    matches = [
        (reference, source, active)
        for reference, reference_active in tracks[interior]
        for source, source_active in tracks[exterior]
        if (active := reference_active) == source_active
    ]
    if not matches:
        return [row[:] for row in grid]
    reference, source, active = max(
        matches,
        key=lambda item: (len(item[2]), -abs(item[0] - separator), -abs(item[1] - separator)),
    )
    reference_line = (
        grid[reference] if axis == 0 else [grid[row][reference] for row in range(height)]
    )
    source_line = grid[source] if axis == 0 else [grid[row][source] for row in range(height)]
    output = [row[:] for row in grid]
    source_background = backgrounds[exterior]
    for coordinate in active:
        if axis == 0:
            output[source][coordinate] = source_background
        else:
            output[coordinate][source] = source_background
    near = separator + exterior
    far = 0 if exterior < 0 else line_length - 1
    for coordinate in active:
        target = near if source_line[coordinate] == reference_line[coordinate] else far
        if axis == 0:
            output[target][coordinate] = source_line[coordinate]
        else:
            output[coordinate][target] = source_line[coordinate]
    return output
