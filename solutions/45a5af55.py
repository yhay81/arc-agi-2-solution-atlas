def _uniform_rows_to_concentric_frames(array):
    height = len(array)
    if height < 2 or any(len(set(row)) != 1 for row in array):
        return [row[:] for row in array]
    colors = [row[0] for row in array]
    if colors[-1] != colors[-2]:
        return [row[:] for row in array]
    side = 2 * (height - 1)
    output = [[0] * side for _ in range(side)]
    for row in range(side):
        for col in range(side):
            depth = min(row, col, side - 1 - row, side - 1 - col)
            output[row][col] = colors[depth]
    return output


def solve(grid):
    return _uniform_rows_to_concentric_frames(grid)
