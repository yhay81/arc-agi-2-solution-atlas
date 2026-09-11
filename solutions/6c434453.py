SQUARE = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
PLUS = [[0, 2, 0], [2, 2, 2], [0, 2, 0]]


def solve(grid):
    output = [row[:] for row in grid]
    for row in range(len(grid) - 2):
        for col in range(len(grid[0]) - 2):
            window = [line[col : col + 3] for line in grid[row : row + 3]]
            if window == SQUARE:
                for offset, line in enumerate(PLUS):
                    output[row + offset][col : col + 3] = line
    return output
