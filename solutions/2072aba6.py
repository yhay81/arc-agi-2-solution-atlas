def _pattern_upscale_five(grid):
    output = [[0] * (len(grid[0]) * 2) for _ in range(len(grid) * 2)]
    for row, line in enumerate(grid):
        for col, value in enumerate(line):
            if value == 5:
                output[row * 2][col * 2 : col * 2 + 2] = [1, 2]
                output[row * 2 + 1][col * 2 : col * 2 + 2] = [2, 1]
    return output


def solve(grid):
    return _pattern_upscale_five(grid)
