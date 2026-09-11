def _recolor_vertical_mirror_pairs(array, source_color=5, target_color=1):
    output = [row[:] for row in array]
    width = len(array[0])
    for row, values in enumerate(array):
        for col, value in enumerate(values):
            if value != source_color:
                continue
            mirror = width - 1 - col
            if array[row][mirror] == source_color:
                output[row][col] = target_color
    return output


def solve(grid):
    return _recolor_vertical_mirror_pairs(grid, 5, 1)
