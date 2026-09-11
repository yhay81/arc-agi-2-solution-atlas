def _mirror_seed_across_separator_cross(array):
    height, width = len(array), len(array[0])
    if height % 2 == 0 or width % 2 == 0:
        return [row[:] for row in array]
    mid_row, mid_col = (height // 2, width // 2)
    separator = array[mid_row][mid_col]
    if separator == 0:
        return [row[:] for row in array]
    if any(v != separator for v in array[mid_row]) or any(
        array[r][mid_col] != separator for r in range(height)
    ):
        return [row[:] for row in array]
    if any(array[r][c] != 0 for r in range(mid_row) for c in range(mid_col + 1, width)) or any(
        array[r][c] != 0 for r in range(mid_row + 1, height) for c in range(width) if c != mid_col
    ):
        return [row[:] for row in array]
    seed = [[separator if array[r][c] != 0 else 0 for c in range(mid_col)] for r in range(mid_row)]
    top = [row + row[::-1] for row in seed]
    return top + top[::-1]


def solve(grid):
    return _mirror_seed_across_separator_cross(grid)
