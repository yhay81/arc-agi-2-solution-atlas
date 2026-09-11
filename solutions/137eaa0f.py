def _compose_3x3_around_markers(array, marker=5):
    positions = [
        (r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == marker
    ]
    if len(positions) < 2:
        return [row[:] for row in array]
    output = [[0] * 3 for _ in range(3)]
    for row, col in positions:
        if row == 0 or col == 0 or row == len(array) - 1 or col == len(array[0]) - 1:
            return [row[:] for row in array]
        neighborhood = [r[col - 1 : col + 2] for r in array[row - 1 : row + 2]]
        for local_row in range(3):
            for local_col in range(3):
                value = neighborhood[local_row][local_col]
                if value == 0:
                    continue
                if output[local_row][local_col] not in (0, value):
                    return [row[:] for row in array]
                output[local_row][local_col] = value
    return output if any(value for row in output for value in row) else [row[:] for row in array]


def solve(grid):
    return _compose_3x3_around_markers(grid)
