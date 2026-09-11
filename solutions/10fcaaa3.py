def _tile_twice_with_diagonal_neighbors(array, fill_color=8):
    output = [row * 2 for row in array] + [row * 2 for row in array]
    sources = [(r, c) for r, row in enumerate(output) for c, v in enumerate(row) if v]
    height, width = len(output), len(output[0])
    for source_row, source_col in sources:
        for delta_row, delta_col in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            row, col = (source_row + delta_row, source_col + delta_col)
            if 0 <= row < height and 0 <= col < width and output[row][col] == 0:
                output[row][col] = fill_color
    return output


def solve(grid):
    return _tile_twice_with_diagonal_neighbors(grid, 8)
