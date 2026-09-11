def _recolor_markers_by_nearest_border(array):
    output = [row[:] for row in array]
    h, w = len(array), len(array[0])
    solid_rows = [
        row
        for row in range(h)
        if array[row][0] != 0 and all(v == array[row][0] for v in array[row])
    ]
    solid_cols = [
        col
        for col in range(w)
        if array[0][col] != 0 and all(array[r][col] == array[0][col] for r in range(h))
    ]
    if len(solid_rows) >= 2:
        first, second = (solid_rows[0], solid_rows[-1])
        first_color, second_color = (array[first][0], array[second][0])
        border_colors = {first_color, second_color}
        for row in range(h):
            for col in range(w):
                if array[row][col] == 0:
                    continue
                if row in (first, second) or array[row][col] in border_colors:
                    continue
                output[row][col] = first_color if row - first < second - row else second_color
        return output
    if len(solid_cols) >= 2:
        first, second = (solid_cols[0], solid_cols[-1])
        first_color, second_color = (array[0][first], array[0][second])
        border_colors = {first_color, second_color}
        for row in range(h):
            for col in range(w):
                if array[row][col] == 0:
                    continue
                if col in (first, second) or array[row][col] in border_colors:
                    continue
                output[row][col] = first_color if col - first < second - col else second_color
    return output


def solve(grid):
    return _recolor_markers_by_nearest_border([row[:] for row in grid])
