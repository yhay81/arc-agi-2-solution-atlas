from itertools import combinations


def _fill_rectangles_between_corners(array, corner_color=4, fill_color=2):
    corners = {
        (r, c)
        for r, row in enumerate(array)
        for c, value in enumerate(row)
        if value == corner_color
    }
    if len(corners) < 4:
        return [row[:] for row in array]
    output = [row[:] for row in array]
    rows = sorted({row for row, _ in corners})
    cols = sorted({col for _, col in corners})
    for top, bottom in combinations(rows, 2):
        for left, right in combinations(cols, 2):
            rectangle = {(top, left), (top, right), (bottom, left), (bottom, right)}
            if rectangle <= corners and bottom > top + 1 and (right > left + 1):
                for row in range(top + 1, bottom):
                    for col in range(left + 1, right):
                        output[row][col] = fill_color
    return output


def solve(grid):
    return _fill_rectangles_between_corners(grid, 4, 2)
