def _fill_plus_shapes(array, color=3):
    output = [row[:] for row in array]
    for row in range(1, len(array) - 1):
        for col in range(1, len(array[0]) - 1):
            if array[row][col] != 0:
                continue
            arms = ((-1, 0), (1, 0), (0, -1), (0, 1))
            if not all(array[row + dr][col + dc] == 0 for dr, dc in arms):
                continue
            for dr, dc in ((0, 0), *arms):
                output[row + dr][col + dc] = color
    return output


def solve(grid):
    output = _fill_plus_shapes(grid, 1)
    color_map = {8: 8, 0: 0, 1: 3}
    source = [row[:] for row in output]
    for old, new in color_map.items():
        for r, row in enumerate(source):
            for c, value in enumerate(row):
                if value == old:
                    output[r][c] = new
    return output
