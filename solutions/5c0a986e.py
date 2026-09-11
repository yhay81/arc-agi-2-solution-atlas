def _extend_one_northwest_two_southeast(array):
    output = [row[:] for row in array]
    for color, row_delta, col_delta, corner in ((1, -1, -1, "top_left"), (2, 1, 1, "bottom_right")):
        positions = [
            (r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == color
        ]
        if not len(positions):
            return [row[:] for row in array]
        top, left = min(positions)
        bottom, right = max(positions)
        top, left = min(r for r, _ in positions), min(c for _, c in positions)
        bottom, right = max(r for r, _ in positions), max(c for _, c in positions)
        if len(positions) != (bottom - top + 1) * (right - left + 1):
            return [row[:] for row in array]
        row, col = (top, left) if corner == "top_left" else (bottom, right)
        row += row_delta
        col += col_delta
        while 0 <= row < len(array) and 0 <= col < len(array[0]):
            if output[row][col] == 0:
                output[row][col] = color
            row += row_delta
            col += col_delta
    return output


def solve(grid):
    return _extend_one_northwest_two_southeast(grid)
