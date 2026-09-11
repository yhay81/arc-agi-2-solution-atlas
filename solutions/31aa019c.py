def _frame_unique_frequency_cell(array, frame_color=2):
    counts = {}
    for row in array:
        for value in row:
            if value != 0:
                counts[value] = counts.get(value, 0) + 1
    unique = [value for value, count in counts.items() if count == 1]
    if len(unique) != 1:
        return [row[:] for row in array]
    positions = [
        (r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == unique[0]
    ]
    if len(positions) != 1:
        return [row[:] for row in array]
    row, col = positions[0]
    output = [[0] * len(array[0]) for _ in array]
    top, bottom = max(0, row - 1), min(len(array), row + 2)
    left, right = max(0, col - 1), min(len(array[0]), col + 2)
    for r in range(top, bottom):
        for c in range(left, right):
            output[r][c] = frame_color
    output[row][col] = unique[0]
    return output


def solve(grid):
    return _frame_unique_frequency_cell(grid)
