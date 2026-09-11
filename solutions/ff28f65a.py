def solve(grid):
    units = sum(cell != 0 for row in grid for cell in row) // 4
    output = [[0] * 3 for _ in range(3)]
    positions = ((0, 0), (0, 2), (1, 1), (2, 0), (2, 2))
    for row, col in positions[:units]:
        output[row][col] = 1
    return output
