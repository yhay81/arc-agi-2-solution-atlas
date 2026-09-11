from collections.abc import Sequence


def _project_lines_by_color(
    array,
    horizontal_colors: Sequence[int] = (1, 3),
    vertical_colors: Sequence[int] = (2,),
):
    vals = [v for row in array for v in row]
    background = max(set(vals), key=vals.count)
    horizontal = {int(value) for value in horizontal_colors}
    vertical = {int(value) for value in vertical_colors}
    output = [[background] * len(array[0]) for _ in array]
    for row, line in enumerate(array):
        for col, color in enumerate(line):
            if color != background and color in vertical:
                for r in range(len(array)):
                    output[r][col] = color
    for row, line in enumerate(array):
        for col, color in enumerate(line):
            if color != background and color in horizontal:
                output[row] = [color] * len(array[0])
    return output


def solve(grid):
    return _project_lines_by_color(grid, [1, 3], [2])
