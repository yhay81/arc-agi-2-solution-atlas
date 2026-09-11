def _border_from_marker(grid):
    values = [v for row in grid for v in row if v != 0]
    if len(values) != 1:
        return [row[:] for row in grid]
    output = [[0] * len(grid[0]) for _ in grid]
    for c in range(len(grid[0])):
        output[0][c] = output[-1][c] = values[0]
    for r in range(len(grid)):
        output[r][0] = output[r][-1] = values[0]
    return output


def solve(grid):
    return _border_from_marker(grid)
