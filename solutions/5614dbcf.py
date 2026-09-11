from collections import Counter


def _compress_three_blocks(array):
    h, w = len(array), len(array[0])
    if h % 3 or w % 3:
        return [row[:] for row in array]
    output = [[0] * (w // 3) for _ in range(h // 3)]
    for row in range(h // 3):
        for col in range(w // 3):
            values = [
                array[r][c]
                for r in range(row * 3, row * 3 + 3)
                for c in range(col * 3, col * 3 + 3)
                if array[r][c] != 5
            ]
            if values:
                color, count = Counter(values).most_common(1)[0]
                if count >= 5:
                    output[row][col] = color
    return output


def solve(grid):
    return _compress_three_blocks(grid)
