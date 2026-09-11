def solve(grid):
    height, width = len(grid), len(grid[0])
    markers = sorted(
        (row, col, value)
        for row, line in enumerate(grid)
        for col, value in enumerate(line)
        if value
    )
    if len(markers) != 2 or markers[0][0] >= markers[1][0]:
        return [row[:] for row in grid]

    split = (markers[0][0] + markers[1][0] + 1) // 2
    output = [[0] * width for _ in range(height)]
    for (marker_row, _, color), (top, bottom, outer_row) in zip(
        markers,
        ((0, split, 0), (split, height, height - 1)),
    ):
        if not top <= marker_row < bottom:
            return [row[:] for row in grid]
        for row in range(top, bottom):
            output[row][0] = color
            output[row][-1] = color
        for col in range(width):
            output[marker_row][col] = color
            output[outer_row][col] = color
    return output
