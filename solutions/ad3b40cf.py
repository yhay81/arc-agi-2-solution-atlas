from collections import Counter


def solve(grid):
    output = [row[:] for row in grid]
    counts = Counter(value for row in grid for value in row)
    background = counts.most_common(1)[0][0]
    mirror = {
        (row, col) for row, line in enumerate(grid) for col, value in enumerate(line) if value == 1
    }
    top = min(row for row, _ in mirror)
    bottom = max(row for row, _ in mirror)
    left = min(col for _, col in mirror)
    right = max(col for _, col in mirror)
    color = min(counts.keys() - {background, 1}, key=counts.get)
    shape = {
        (row, col)
        for row, line in enumerate(grid)
        for col, value in enumerate(line)
        if value == color
    }
    if left == right:
        reflected = {(row, 2 * left - col) for row, col in shape}
    elif top == bottom:
        reflected = {(2 * top - row, col) for row, col in shape}
    elif (top, left) in mirror:
        reflected = {(top + col - left, left + row - top) for row, col in shape}
    else:
        reflected = {(top + right - col, top + right - row) for row, col in shape}
    for row, col in reflected:
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            output[row][col] = color
    return output
