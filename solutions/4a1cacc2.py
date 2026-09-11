def _extend_marker_to_corner(array):
    counts = {}
    for row in array:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    values = list(counts)
    if len(values) < 2:
        return [row[:] for row in array]
    background = max(values, key=counts.get)
    positions = [
        (r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value != background
    ]
    if len(positions) != 1:
        return [row[:] for row in array]
    row, col = positions[0]
    color = array[row][col]
    corners = (
        (0, 0),
        (0, len(array[0]) - 1),
        (len(array) - 1, 0),
        (len(array) - 1, len(array[0]) - 1),
    )
    corner = min(corners, key=lambda item: abs(item[0] - row) + abs(item[1] - col))
    output = [item[:] for item in array]
    top, bottom = sorted((row, corner[0]))
    left, right = sorted((col, corner[1]))
    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            output[r][c] = color
    return output


def solve(grid):
    return _extend_marker_to_corner(grid)
