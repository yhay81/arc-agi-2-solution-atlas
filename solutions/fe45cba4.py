def _rectangularize_largest_color(array):
    counts = {v: sum(row.count(v) for row in array) for v in set(v for row in array for v in row)}
    values = list(counts)
    background = max(values, key=counts.get)
    colors = [v for v in values if v != background]
    if len(colors) < 2:
        return [r[:] for r in array]
    largest = max(colors, key=lambda color: counts[color])
    positions = [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v == largest]
    area = len(positions)
    if area < 2:
        return [r[:] for r in array]
    best_rows = 1
    for rows in range(1, int(area**0.5) + 1):
        if area % rows == 0:
            best_rows = rows
    rows, cols = (best_rows, area // best_rows)
    top, bottom = min(r for r, c in positions), max(r for r, c in positions)
    right = max(c for r, c in positions)
    start_row = top if top == 0 else bottom - rows + 1
    start_col = right - cols + 1
    if start_row < 0 or start_col < 0:
        return [r[:] for r in array]
    output = [r[:] for r in array]
    for r, c in positions:
        output[r][c] = background
    for r in range(start_row, start_row + rows):
        for c in range(start_col, start_col + cols):
            output[r][c] = largest
    return output


def solve(grid):
    return _rectangularize_largest_color([r[:] for r in grid])
