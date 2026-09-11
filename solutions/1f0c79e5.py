def _propagate_marker_tile_diagonals(array, marker=2):
    positions = [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v]
    if not len(positions):
        return [r[:] for r in array]
    top, left = min(positions)
    bottom, right = max(positions)
    if (bottom - top + 1, right - left + 1) != (2, 2):
        return [r[:] for r in array]
    tile = [row[left : right + 1] for row in array[top : bottom + 1]]
    colors = sorted({v for row in tile for v in row if v})
    if int(marker) not in colors or len(colors) != 2:
        return [r[:] for r in array]
    drawing = next(color for color in colors if color != int(marker))
    marker_cells = [(r, c) for r, row in enumerate(tile) for c, v in enumerate(row) if v == marker]
    if not len(marker_cells):
        return [r[:] for r in array]
    output = [[0] * len(array[0]) for _ in array]
    tile_mask = [(r, c) for r, row in enumerate(tile) for c, v in enumerate(row) if v]
    for cell in marker_cells:
        direction = (-1 if cell[0] == 0 else 1, -1 if cell[1] == 0 else 1)
        if not all(direction):
            return [r[:] for r in array]
        for offset in range(max(len(array), len(array[0])) + 2):
            origin_row = int(top + offset * direction[0])
            origin_col = int(left + offset * direction[1])
            if (
                origin_row + 1 < 0
                or origin_row >= len(array)
                or origin_col + 1 < 0
                or origin_col >= len(array[0])
            ):
                break
            for row, col in tile_mask:
                out_row, out_col = origin_row + row, origin_col + col
                if 0 <= out_row < len(array) and 0 <= out_col < len(array[0]):
                    output[out_row][out_col] = drawing
    return output


def solve(grid):
    array = [r[:] for r in grid]
    output = _propagate_marker_tile_diagonals(array, 2)
    return output
