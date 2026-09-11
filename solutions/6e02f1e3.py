def _unique_color_glyph(grid):
    color_count = len({value for row in grid for value in row})
    output = [[0] * 3 for _ in range(3)]
    if color_count == 1:
        output[0] = [5] * 3
    elif color_count == 2:
        for i in range(3):
            output[i][i] = 5
    elif color_count == 3:
        for i in range(3):
            output[i][2 - i] = 5
    else:
        return [row[:] for row in grid]
    return output


def solve(grid):
    return _unique_color_glyph(grid)
