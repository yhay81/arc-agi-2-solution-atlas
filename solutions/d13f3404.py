def _diagonal_repeat(array):
    height, width = len(array), len(array[0])
    output = [[0] * (width * 2) for _ in range(height * 2)]
    for offset in range(min(height, width) * 2):
        bottom = min(height + offset, height * 2)
        right = min(width + offset, width * 2)
        for r in range(offset, bottom):
            for c in range(offset, right):
                value = array[r - offset][c - offset]
                if value != 0:
                    output[r][c] = value
    return output


def solve(grid):
    return _diagonal_repeat(grid)
