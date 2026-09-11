def _mark_zero_lines_inside_border(array, marker=3):
    source = [row[:] for row in array]
    if len(source) < 3 or len(source[0]) < 3:
        return source
    inner = [row[1:-1] for row in source[1:-1]]
    marked = set()
    for row in range(len(inner)):
        if all(value == 0 for value in inner[row]):
            marked.update((row, col) for col in range(len(inner[0])))
    for col in range(len(inner[0])):
        if all(inner[row][col] == 0 for row in range(len(inner))):
            marked.update((row, col) for row in range(len(inner)))
    output = [row[:] for row in source]
    for row, col in marked:
        target_row, target_col = row + 1, col + 1
        if output[target_row][target_col] == 0:
            output[target_row][target_col] = marker
    return output


def solve(grid):
    return _mark_zero_lines_inside_border(grid, 3)
