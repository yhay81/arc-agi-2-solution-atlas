def _count_marker_in_lattice(array, separator=8, target=6, threshold=2):
    height, width = len(array), len(array[0])
    separator_rows = [r for r in range(height) if all(v == separator for v in array[r])]
    separator_cols = [
        c for c in range(width) if all(array[r][c] == separator for r in range(height))
    ]
    if not separator_rows or not separator_cols:
        return [r[:] for r in array]
    row_starts = [0, *(row + 1 for row in separator_rows)]
    row_ends = [*separator_rows, height]
    col_starts = [0, *(col + 1 for col in separator_cols)]
    col_ends = [*separator_cols, width]
    output = [[0] * len(col_starts) for _ in row_starts]
    for row_index, (top, bottom) in enumerate(zip(row_starts, row_ends, strict=True)):
        for col_index, (left, right) in enumerate(zip(col_starts, col_ends, strict=True)):
            if (
                sum(array[r][c] == target for r in range(top, bottom) for c in range(left, right))
                == threshold
            ):
                output[row_index][col_index] = 1
    return output


def solve(grid):
    array = [r[:] for r in grid]
    output = _count_marker_in_lattice(array, 8, 6, 1)
    color_map = {1: 0, 0: 1}
    source = [r[:] for r in output]
    for old, new in color_map.items():
        for r in range(len(output)):
            for c in range(len(output[0])):
                if source[r][c] == old:
                    output[r][c] = new
    return output
