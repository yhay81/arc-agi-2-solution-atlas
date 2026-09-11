def _join_row_endpoints_with_center_marker(array, center_color=5):
    output = [row[:] for row in array]
    for row in range(len(array)):
        columns = [c for c, value in enumerate(array[row]) if value != 0]
        if len(columns) != 2:
            continue
        left, right = columns
        if right - left < 2 or (left + right) % 2:
            continue
        midpoint = (left + right) // 2
        output[row][left:midpoint] = [array[row][left]] * (midpoint - left)
        output[row][midpoint] = center_color
        output[row][midpoint + 1 : right + 1] = [array[row][right]] * (right - midpoint)
    return output


def solve(grid):
    return _join_row_endpoints_with_center_marker(grid)
