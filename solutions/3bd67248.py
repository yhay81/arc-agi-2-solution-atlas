def _corner_completion(array, side):
    output = [row[:] for row in array]
    h, w = len(array), len(array[0])
    if (
        side == "left"
        and all(row[0] != 0 for row in array)
        and not any(v != 0 for row in array for v in row[1:])
    ):
        for row in range(max(0, h - 1)):
            col = w - 1 - row
            if 0 <= col < w:
                output[row][col] = 2
        for c in range(1, w):
            output[-1][c] = 4
        return output
    if (
        side == "right"
        and all(row[-1] != 0 for row in array)
        and not any(v != 0 for row in array for v in row[:-1])
    ):
        for row in range(max(0, h - 1)):
            col = row
            if col < w:
                output[row][col] = 2
        for c in range(w - 1):
            output[-1][c] = 4
        return output
    return [row[:] for row in array]


def solve(grid):
    return _corner_completion(grid, "left")
