def _right_rays_with_boundary_tails(array):
    output = [row[:] for row in array]
    marker_rows = [row for row in range(len(array)) if any(value != 0 for value in array[row])]
    for index, row in enumerate(marker_rows):
        positions = [c for c, value in enumerate(array[row]) if value != 0]
        if len(positions) != 1:
            continue
        col = positions[0]
        color = array[row][col]
        output[row][col:] = [color] * (len(array[0]) - col)
        stop = marker_rows[index + 1] if index + 1 < len(marker_rows) else len(array)
        if row + 1 < stop:
            for r in range(row + 1, stop):
                output[r][-1] = color
    return output


def solve(grid):
    return _right_rays_with_boundary_tails(grid)
