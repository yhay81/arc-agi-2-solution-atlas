def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]

    horizontal = {}
    for row in range(height):
        for left in range(width - 1):
            for right in range(left + 1, width):
                values = grid[row][left : right + 1]
                missing = [index for index, value in enumerate(values) if value != 5]
                wall = not missing or (
                    len(missing) == 1
                    and (
                        (right == width - 1 and missing[0] == len(values) - 1)
                        or (left == 0 and missing[0] == 0)
                    )
                    and values[missing[0]] == 0
                )
                horizontal[row, left, right] = wall, not missing

    column_non_gray = [[0] * (height + 1) for _ in range(width)]
    for col in range(width):
        for row in range(height):
            column_non_gray[col][row + 1] = column_non_gray[col][row] + (grid[row][col] != 5)

    candidates = []
    for top in range(height - 1):
        for bottom in range(top + 1, height):
            for left in range(width - 1):
                for right in range(left + 1, width):
                    (top_wall, top_full) = horizontal[top, left, right]
                    (bottom_wall, bottom_full) = horizontal[bottom, left, right]
                    if not top_wall or not bottom_wall:
                        continue
                    if left > 0 and column_non_gray[left][bottom] != column_non_gray[left][top + 1]:
                        continue
                    if (
                        right < width - 1
                        and column_non_gray[right][bottom] != column_non_gray[right][top + 1]
                    ):
                        continue
                    if sum((top_full, bottom_full, left > 0, right < width - 1)) < 3:
                        continue

                    row_start, row_stop = top + 1, bottom
                    col_start = left + 1 if left > 0 else 0
                    col_stop = right if right < width - 1 else right + 1
                    region = [grid[row][col_start:col_stop] for row in range(row_start, row_stop)]
                    if (
                        not region
                        or not region[0]
                        or any(value not in (0, 5) for row in region for value in row)
                    ):
                        continue
                    if (left == 0 or right == width - 1) and any(
                        value == 5 for row in region for value in row[1:-1]
                    ):
                        continue
                    cells = {
                        (row, col)
                        for row in range(row_start, row_stop)
                        for col in range(col_start, col_stop)
                        if grid[row][col] == 0
                    }
                    if left == 0 and right < width - 1 and len(cells) > 2:
                        continue
                    if cells:
                        candidates.append((len(cells), cells))

    remaining = candidates[:]
    while remaining:
        _, cells = min(remaining, key=lambda item: item[0])
        remaining = [item for item in remaining if not cells.intersection(item[1])]
        for row, col in cells:
            output[row][col] = 4
    return output
