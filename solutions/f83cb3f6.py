def solve(grid):
    height, width = len(grid), len(grid[0])
    values = sorted({value for row in grid for value in row})
    counts = {value: sum(row.count(value) for row in grid) for value in values}
    background = max(values, key=lambda value: counts[value])
    candidates = []
    for color in values:
        if color == background:
            continue
        for row in range(height):
            cells = [(row, col) for col in range(width) if grid[row][col] == color]
            if len(cells) >= 3:
                candidates.append((len(cells), cells, "horizontal", row, color))
        for col in range(width):
            cells = [(row, col) for row in range(height) if grid[row][col] == color]
            if len(cells) >= 3:
                candidates.append((len(cells), cells, "vertical", col, color))
    if not candidates:
        return [row[:] for row in grid]
    _, separator, orientation, coordinate, separator_color = max(
        candidates, key=lambda item: item[0]
    )
    span = (
        {col for _, col in separator}
        if orientation == "horizontal"
        else {row for row, _ in separator}
    )
    output = [[background] * width for _ in range(height)]
    for row, col in separator:
        output[row][col] = separator_color
    for row in range(height):
        for col in range(width):
            if grid[row][col] == background or (row, col) in separator:
                continue
            if orientation == "horizontal" and col in span:
                target = coordinate - 1 if row < coordinate else coordinate + 1
                if 0 <= target < height:
                    output[target][col] = grid[row][col]
            elif orientation == "vertical" and row in span:
                target = coordinate - 1 if col < coordinate else coordinate + 1
                if 0 <= target < width:
                    output[row][target] = grid[row][col]
    return output
