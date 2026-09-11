def solve(grid):
    marked = sum(cell != 0 for row in grid for cell in row)
    output = [[0] * 3 for _ in range(3)]
    positions = ((0, 0), (0, 1), (0, 2), (1, 1))
    for row, col in positions[:marked]:
        output[row][col] = 2
    return output
