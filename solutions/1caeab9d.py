def _align_components_to_reference(array, reference_color=1):
    h, w = len(array), len(array[0])
    reference_rows = [r for r in range(h) for c in range(w) if array[r][c] == reference_color]
    if not reference_rows:
        return [row[:] for row in array]
    reference_top = min(reference_rows)
    output = [[0] * w for _ in range(h)]
    colors = sorted({value for row in array for value in row if value != 0})
    for color in colors:
        cells = [(r, c) for r in range(h) for c in range(w) if array[r][c] == color]
        top = min(r for r, _ in cells)
        row_shift = 0 if color == reference_color else reference_top - top
        for row, col in cells:
            target_row = row + row_shift
            if 0 <= target_row < h:
                output[target_row][col] = color
    return output


def solve(grid):
    return _align_components_to_reference(grid, 1)
