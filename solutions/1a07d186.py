def _snap_markers_to_matching_lines(array):
    output = [row[:] for row in array]
    height, width = len(output), len(output[0])
    guides: dict[int, list[tuple[int, int]]] = {}
    for row in range(height):
        if len(set(output[row])) == 1 and output[row][0] != 0:
            guides.setdefault(output[row][0], []).append((0, row))
    for col in range(width):
        if len({output[r][col] for r in range(height)}) == 1 and output[0][col] != 0:
            guides.setdefault(output[0][col], []).append((1, col))
    guide_cells = {
        (row, col)
        for entries in guides.values()
        for axis, index in entries
        for row in (range(height) if axis == 1 else (index,))
        for col in (range(width) if axis == 0 else (index,))
    }
    result = [[0] * width for _ in range(height)]
    for row, col in guide_cells:
        result[row][col] = output[row][col]
    for row in range(height):
        for col in range(width):
            if output[row][col] == 0:
                continue
            color = output[row][col]
            if (row, col) in guide_cells or color not in guides:
                continue
            entries = guides[color]
            axis, index = min(
                entries, key=lambda item: abs((row if item[0] == 0 else col) - item[1])
            )
            distance = (row if axis == 0 else col) - index
            snapped = index - 1 if distance < 0 else index + 1
            if 0 <= snapped < (height if axis == 0 else width):
                if axis == 0:
                    result[snapped][col] = color
                else:
                    result[row][snapped] = color
    return result


def solve(grid):
    return _snap_markers_to_matching_lines([row[:] for row in grid])
