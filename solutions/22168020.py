from itertools import pairwise


def _fill_between_same(array):
    output = [row[:] for row in array]
    for row in range(len(array)):
        positions = [c for c, v in enumerate(array[row]) if v != 0]
        if len(positions) < 2:
            continue
        for left, right in pairwise(positions):
            if array[row][left] == array[row][right]:
                output[row][left : right + 1] = [array[row][left]] * (right - left + 1)
    for col in range(len(array[0])):
        positions = [r for r in range(len(array)) if array[r][col] != 0]
        if len(positions) < 2:
            continue
        for top, bottom in pairwise(positions):
            if array[top][col] == array[bottom][col]:
                for r in range(top, bottom + 1):
                    output[r][col] = array[top][col]
    return output


def solve(grid):
    return _fill_between_same(grid)
