def _recolor_empty_rows_and_columns_two(array):
    empty_rows = [r for r, row in enumerate(array) if all(v == 0 for v in row)]
    empty_cols = [c for c in range(len(array[0])) if all(row[c] == 0 for row in array)]
    if not len(empty_rows) and (not len(empty_cols)):
        return [row[:] for row in array]
    output = [row[:] for row in array]
    for r in empty_rows:
        output[r] = [2] * len(array[0])
    for c in empty_cols:
        for r in range(len(array)):
            output[r][c] = 2
    return output


def solve(grid):
    return _recolor_empty_rows_and_columns_two(grid)
