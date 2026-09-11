def _draw_x_holes(grid):
    size = len(grid)
    if size != len(grid[0]) or size % 2 == 0:
        return [row[:] for row in grid]
    counts = [sum(value == color for row in grid for value in row) for color in range(10)]
    background = max(range(10), key=lambda color: (counts[color], -color))
    if sum(value != background for row in grid for value in row) > 1:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for i in range(size):
        output[i][i] = 0
        output[i][size - 1 - i] = 0
    return output


def solve(grid):
    return _draw_x_holes(grid)
