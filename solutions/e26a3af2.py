from collections import Counter


def _denoise_axis_aligned_regions(array):
    if not array or not array[0]:
        return [row[:] for row in array]

    def mode(values):
        return Counter(values).most_common(1)[0][0]

    h, w = len(array), len(array[0])
    row_colors = [mode(row) for row in array]
    col_colors = [mode([array[r][c] for r in range(h)]) for c in range(w)]
    row_render = [[row_colors[r]] * w for r in range(h)]
    col_render = [[col_colors[c] for c in range(w)] for _ in range(h)]
    row_error = sum(array[r][c] != row_render[r][c] for r in range(h) for c in range(w))
    col_error = sum(array[r][c] != col_render[r][c] for r in range(h) for c in range(w))
    if row_error == col_error:
        return [row[:] for row in array]
    return row_render if row_error < col_error else col_render


def solve(grid):
    return _denoise_axis_aligned_regions(grid)
