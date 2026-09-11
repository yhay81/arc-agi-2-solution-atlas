def _expand_vertical_seven_line_into_cone(array):
    occupied = [(r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value != 0]
    if not occupied or {value for row in array for value in row} - {0, 7}:
        return [row[:] for row in array]
    cols = {c for _, c in occupied}
    rows = sorted({r for r, _ in occupied})
    if len(cols) != 1 or rows != list(range(rows[0], rows[-1] + 1)):
        return [row[:] for row in array]
    center_col = next(iter(cols))
    top, bottom = rows[0], rows[-1]
    if top == bottom:
        return [row[:] for row in array]
    output = [row[:] for row in array]
    for row in range(top, bottom + 1):
        radius = bottom - row
        for col in range(max(0, center_col - radius), min(len(array[0]), center_col + radius + 1)):
            output[row][col] = 7 if abs(col - center_col) % 2 == 0 else 8
    return output


def solve(grid):
    return _expand_vertical_seven_line_into_cone(grid)
