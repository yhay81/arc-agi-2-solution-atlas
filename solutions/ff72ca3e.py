def _draw_square_by_nearest_marker(array, center_color=4, boundary_color=5, fill_color=2):
    centers = [
        (r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v == center_color
    ]
    boundaries = [
        (r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v == boundary_color
    ]
    if not len(centers) or not len(boundaries):
        return [r[:] for r in array]
    output = [r[:] for r in array]
    for row, col in centers:
        radius = min(max(abs(r - row), abs(c - col)) for r, c in boundaries) - 1
        if radius < 1:
            continue
        for target_row in range(int(row) - radius, int(row) + radius + 1):
            for target_col in range(int(col) - radius, int(col) + radius + 1):
                if (
                    0 <= target_row < len(array)
                    and 0 <= target_col < len(array[0])
                    and output[target_row][target_col] == 0
                ):
                    output[target_row][target_col] = fill_color
    return output


def solve(grid):
    array = [r[:] for r in grid]
    output = _draw_square_by_nearest_marker(array, 4, 5, 1)
    color_map = {0: 0, 5: 5, 1: 2, 4: 4}
    source = [r[:] for r in output]
    for old, new in color_map.items():
        for r in range(len(output)):
            for c in range(len(output[0])):
                if source[r][c] == old:
                    output[r][c] = new
    return output
