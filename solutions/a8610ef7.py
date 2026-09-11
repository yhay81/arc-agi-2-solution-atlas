def _recolor_by_vertical_symmetry(array, source_color=8, symmetric_color=2, asymmetric_color=5):
    output = [row[:] for row in array]
    height = len(array)
    for row, line in enumerate(array):
        for col, value in enumerate(line):
            if value != source_color:
                continue
            mirror = height - 1 - row
            output[row][col] = (
                symmetric_color if array[mirror][col] == source_color else asymmetric_color
            )
    return output


def solve(grid):
    output = _recolor_by_vertical_symmetry(grid, 8, 1, 2)
    color_map = {0: 0, 1: 2, 2: 5}
    source = [row[:] for row in output]
    for old, new in color_map.items():
        for r, row in enumerate(source):
            for c, value in enumerate(row):
                if value == old:
                    output[r][c] = new
    return output
